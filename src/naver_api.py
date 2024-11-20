# 네이버 검색 API 예제 - 블로그 검색
import os
import sys
import urllib.request
import pandas as pd
import json
import re

client_id = "PoDH_g_ZdPR_qMptIdj4"
client_secret = ""

query = urllib.parse.quote(input("보고싶은 키워드: "))
idx = 0
display = 100
start = 1
end = 1000
sort = "sim"

news_df = pd.DataFrame(columns=("Title","Original Link", "Link", "Description", "Publication Date"))

for start_idx in range(start, end, display):

    url = "https://openapi.naver.com/v1/search/news?query=" + query \
                + "&display=" + str(display) \
                + "&start=" + str(start_idx) \
                + "&sort=" + sort

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_dict = json.loads(response_body.decode('utf-8'))
        items = response_dict['items']
        for item_index in range(0, len(items)):
            remove_tag = re.compile('<.*?>')
            title = re.sub(remove_tag, '', items[item_index]['title'])
            original_link = items[item_index]['originallink']
            link = items[item_index]['link']
            description = re.sub(remove_tag, '', items[item_index]['description'])
            pub_date = items[item_index]['pubDate']
            news_df.loc[idx] = [title, original_link, link, description, pub_date]
            idx += 1

    else:
        print("Error Code:" + rescode)

news_df