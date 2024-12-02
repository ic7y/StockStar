from app import db
from flask import Blueprint, render_template, request
from common.libs.Helper import *
from common.models.user import User
from common.libs.UserService import UserService
from common.libs.DateHelper import *

register_page = Blueprint("register_page", __name__, url_prefix="/StockStar")


@register_page.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        req = request.values
        login_name = req['login_name'].encode("utf8") if "login_name" in req else ""
        login_pwd = req['login_pwd'] if "login_pwd" in req else ""
        login_pwd2 = req['login_pwd2'] if "login_pwd2" in req else ""

        # 防止attacker绕过前端JS检测，这里再对数据校验一遍
        if login_name is None or len(login_name) < 1:
            return ops_responseErrorJson(code=-1, msg="用户名校验失败，请重新输入~~")
        if login_pwd is None or len(login_pwd) < 6:
            return ops_responseErrorJson(code=-1, msg="密码校验失败，请重新输入~~")
        if login_pwd != login_pwd2:
            return ops_responseErrorJson(code=-1, msg="两次密码不一致，请重新输入~~")

        # 数据库检测
        if User.query.filter_by(login_name=login_name).first():
            return ops_responseErrorJson(code=-1, msg="用户名已存在！")

        user = User()
        user.login_name = login_name

        user.login_salt = UserService.genSalt(8)
        user.login_password = UserService.genPwd(login_pwd, user.login_salt)
        user.created_time = user.updated_time = getCurrentTime()
        db.session.add(user)
        db.session.commit()

        return ops_responseJson(code=200, msg="注册成功！")
