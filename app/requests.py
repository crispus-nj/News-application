from app import app
import requests
from .config import Config
import os
from .models import news_article

News_article = news_article.News_Article

Api_key = os.getenv('API_KEY')
tech_base_url = app.config['TECH_CRUNCH_BASE_URL']
business_base_url=app.config['BUSINESS_BASE_URL']
all_article_base_url= app.config['ALL_ARTICLES_BASE_URL']

def tech_news():
    base_url = tech_base_url.format(Api_key)
    tech_data = requests.get(base_url).json()
    for tech in tech_data['articles']:
        print(tech['author'])
    return tech_data

def all_articles_news():
    '''
    all_articles_news function displays all news from various sources without specification
    '''
    base_url = all_article_base_url.format(Api_key)
    all_article_data = requests.get(base_url).json()
    return all_article_data

