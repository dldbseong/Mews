import requests
from bs4 import BeautifulSoup

# 크롤링 대상 URL
url = "https://news.naver.com/section/100"

# HTML 가져오기
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()  # 요청이 성공했는지 확인

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 기사 정보가 담긴 요소 선택
articles = soup.select('li.sa_item._SECTION_HEADLINE')

# 크롤링 결과 저장
news_data = []
for article in articles:
    try:
        title = article.select_one('a.sa_text_title').get_text(strip=True)
        summary = article.select_one('div.sa_text_lede').get_text(strip=True)
        link = article.select_one('a.sa_text_title')['href']
        
        # 이미지 URL 처리 (src 또는 기본값)
        img_tag = article.select_one('img._LAZY_LOADING')
        image_url = img_tag.get('src') if img_tag and img_tag.get('src') else "이미지 없음"
        
        # 데이터 저장
        news_data.append({
            "title": title,
            "summary": summary,
            "link": link,
            "image_url": image_url
        })
    except AttributeError:
        # 특정 요소가 없는 경우 생략
        continue

# 결과 출력
for news in news_data:
    print(f"제목: {news['title']}")
    print(f"요약: {news['summary']}")
    print(f"링크: {news['link']}")
    print(f"이미지 URL: {news['image_url']}")
    print("-" * 50)
