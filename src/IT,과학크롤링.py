import requests
from bs4 import BeautifulSoup

# 크롤링 대상 URL
url = "https://news.naver.com/section/104"

# HTML 가져오기
response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
response.raise_for_status()  # 요청 성공 여부 확인

# BeautifulSoup으로 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 헤드라인 클래스 선택
headline_classes = [
    'li.sa_item._SECTION_HEADLINE',           # 일반 헤드라인
    'li.sa_item._SECTION_HEADLINE.is_blind'  # 숨겨진 헤드라인
]

# 기사 정보 크롤링
news_data = []
for headline_class in headline_classes:
    articles = soup.select(headline_class)  # 클래스별 기사 선택
    for article in articles:
        try:
            # 제목
            title = article.select_one('a.sa_text_title').get_text(strip=True)
            # 요약
            summary = article.select_one('div.sa_text_lede').get_text(strip=True)
            # 링크
            link = article.select_one('a.sa_text_title')['href']
            # 링크가 상대경로인 경우 절대경로로 변환
            link = f"https://n.news.naver.com{link}" if link.startswith('/') else link

            # 이미지 URL 가져오기
            img_tag = article.select_one('div.sa_thumb img')  # 이미지 태그 선택
            if img_tag and 'src' in img_tag.attrs:  # src 속성이 있는 경우
                image_url = img_tag['src']
            else:
                image_url = "이미지 없음"  # src가 없으면 기본값

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

# 최대 10개의 기사 출력
for index, news in enumerate(news_data[:10]):
    print(f"[{index + 1}] 제목: {news['title']}")
    print(f"요약: {news['summary']}")
    print(f"링크: {news['link']}")
    print(f"이미지 URL: {news['image_url']}")
    print("-" * 50)
