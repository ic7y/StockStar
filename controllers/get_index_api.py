from flask import Blueprint, render_template, request, make_response
from sqlalchemy import text

from app import *
from common.libs.Helper import *

from common.libs.UserService import *
from common.models.stock_index import *

get_index_api_page = Blueprint("get_index_api_page", __name__, url_prefix="/StockStar/api")


@get_index_api_page.route("/get_index_api")
def get_index():
    res = []
    index_list = StockIndex.query
    for index in index_list:
        res.append(index.to_json())
    return make_response(ops_responseJson(data=res))
