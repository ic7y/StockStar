from flask import request, g
from app import *
from common.models.user import User
from common.libs.UserService import UserService


@app.before_request
def before_request():

    user_info = check_login()
    g.current_user = None

    if user_info:
        g.current_user = user_info

    return


# 通过获取cookie判断用户是否登录
def check_login():
    cookies = request.cookies
    cookie_name = app.config['AUTH_COOKIE_NAME']
    auth_cookie = cookies[cookie_name] if cookie_name in cookies else None
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False

    try:
        user_info = User.query.filter_by(id=auth_info[1]).first()
    except Exception:
        return False

    if user_info is None:
        return False

    # genAuthCode方法生成的是由数据库信息散列的MD5，和用户浏览器传入的cookie进行对比
    if auth_info[0] != UserService.genAuthCode(user_info):
        return False

    return user_info
