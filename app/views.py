from app import app
from flask import render_template
from .requests import tech_news
@app.route('/')
def homepage():
    '''
    homepage function runs everytime the application is runned without any routes attached
    '''
    tech_link = tech_news()

    return render_template('index.html', tech_link=tech_link)