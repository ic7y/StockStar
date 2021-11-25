from flask import Blueprint
from common.libs.Helper import ops_render
from common.models.post import *
from common.models.user import *
from sqlalchemy.sql import text

forum_page = Blueprint("forum_page", __name__, url_prefix="/StockStar")


@forum_page.route('/forum')
def forum():
    posts = Post.query.order_by(text("created_time desc"))
    userCount = User.query.count()
    postCount = Post.query.count()
    context = {'data': posts, 'userCount': userCount, 'postCount': postCount}

    return ops_render("forum.html", context)
