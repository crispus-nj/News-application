from app import app
from flask import render_template
from .requests import tech_news, all_articles_news, business_news, apple_news

@app.route('/')
def homepage():
    article_data = all_articles_news()
    business_data = business_news()
    apple_data = apple_news()
    return render_template('index.html', article_data = article_data, business_data=business_data, apple_data=apple_data)

@app.route('/tech-crunch')
def tech_crunch():
    '''
    homepage function runs everytime the application is runned without any routes attached
    '''
    tech_link = tech_news()

    return render_template('tech.html', tech_link=tech_link)
