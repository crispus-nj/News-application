from app import app
import requests
from .config import Config
import os

Api_key = os.getenv('API_KEY')
tech_base_url = app.config['TECH_CRUNCH_BASE_URL']
business_base_url=app.config['BUSINESS_BASE_URL']

def tech_news():
    base_url = tech_base_url.format(Api_key)
    tech_data = requests.get(base_url).json()
    for tech in tech_data['articles']:
        print(tech['author'])
    return tech_data
