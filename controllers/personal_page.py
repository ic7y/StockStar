from flask import Blueprint
from common.libs.Helper import ops_render
from common.models.post import *
from sqlalchemy.sql import text

personal_page = Blueprint("personal_page", __name__, url_prefix="/StockStar")


@personal_page.route('/personal_page/<uname>')
def get_personal_page(uname):
    posts = Post.query.filter_by(blogger=uname).order_by(text("created_time desc"))

    context = {'data': posts}
    return ops_render('personal_page.html', context)
