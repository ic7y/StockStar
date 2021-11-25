from app import db, app
from flask import Blueprint, g
from common.libs.Helper import ops_render
from common.models import user, news, post


index_page = Blueprint("index_page", __name__, url_prefix="/StockStar")


@index_page.route("/index")
def index():

    newsList = news.News().query
    userCount = user.User.query.count()
    postCount = post.Post.query.count()

    context = {'userCount': userCount, 'postCount': postCount, 'news': newsList}
    return ops_render("index.html", context)
