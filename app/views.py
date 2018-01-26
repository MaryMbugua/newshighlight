from flask import render_template
from app import app

##views
@app.route('/')
def index():
    '''
    view root page function that returns the index page
    and its data
    '''
    title = 'Home - Welcome to The best News Update Website Online'
    return render_template('index.html',title = title)

@app.route('/article/<int:article_id>')
def article(article_id):
    '''
    view news article page function that returns the news article
    and its data
    '''
    id = article_id
    title = f'News Article - {id}'
    return render_template('article.html',title = title)