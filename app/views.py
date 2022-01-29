from app import app
from flask import render_template

@app.route('/')
def homepage():
    '''
    homepage function runs everytime the application is runned without any routes attached
    '''
    return render_template('index.html')