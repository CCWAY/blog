
from flask import Blueprint, render_template, session

from back.models import Article, User, ArticleType

web_blue = Blueprint('web', __name__)


@web_blue.route('/index/')
def index():
    user_id = session['user_id']
    user = User.query.get(user_id)
    articles = Article.query.limit(10).all()
    types = ArticleType.query.all()

    return render_template('web/index.html', articles=articles, types=types, user=user)


@web_blue.route('/article/')
def article():
    user_id = session['user_id']
    user = User.query.get(user_id)
    articles = Article.query.all()
    types = ArticleType.query.all()
    count_type = []
    for art in articles:
        count_type.append(art.type)
    return render_template('web/article.html', articles=articles, types=types, count_type=count_type)


@web_blue.route('/a_type/<int:id>/')
def a_type(id):
    articles = Article.query.filter(id == Article.type).all()
    print(articles)
    type = ArticleType.query.get(id)
    return render_template('web/a_type.html', type=type, articles=articles)


@web_blue.route('/message/')
def message():
    articles = Article.query.all()
    return render_template('web/message.html', articles=articles)


@web_blue.route('/read/<int:id>/')
def read(id):
    article = Article.query.get(id)
    user_id = session['user_id']
    user = User.query.get(user_id)
    return render_template('web/read.html', article=article, user=user)


@web_blue.route('/about/')
def about():
    articles = Article.query.all()
    return render_template('web/about.html', articles=articles)
