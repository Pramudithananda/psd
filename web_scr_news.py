import requests
from bs4 import BeautifulSoup

def get_news_highlights(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    news_highlights = []

    headline_tags = ['h1', 'h2', 'h3', 'span']  # Include 'span' tag

    for tag in headline_tags:
        for headline in soup.find_all(tag):
            if tag == 'span' and 'container__headline-text' not in headline.get('class', []):
                continue  # Skip if the span tag doesn't have the required class

            parent_link = headline.find_parent('a')

            if parent_link:
                news_highlights.append({
                    'title': headline.text.strip(),
                })
            #   break  # Stop searching once a headline is found

    return news_highlights

if __name__ == '__main__':
    news_sites = {
        'CNN': 'https://edition.cnn.com/',
        'BBC': 'https://www.bbc.com/news',
        'Fox News': 'https://www.foxnews.com/',
        'NBC': 'https://www.nbcnews.com/world',
        'NPR':'https://www.npr.org/',
    }

    for news_site, url in news_sites.items():
        print(f'News from {news_site}:')

        news_highlights = get_news_highlights(url)

        for highlight in news_highlights:
            print(f'  - {highlight["title"]}')

        print()
