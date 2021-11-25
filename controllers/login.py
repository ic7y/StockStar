from flask import Blueprint, render_template, request, make_response
from app import *
from common.libs.Helper import *
from common.models.user import *
from common.libs.UserService import *

login_page = Blueprint("login_page", __name__, url_prefix="/StockStar")


@login_page.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        req = request.values
        login_name = req['login_name'] if 'login_name' in req else ""
        login_pwd = req['login_pwd'] if 'login_pwd' in req else ""
        if login_name is None or len(login_name) < 1:
            return ops_responseErrorJson(msg="用户名不合法，请重新输入~~")
        if login_pwd is None or len(login_pwd) < 6:
            return ops_responseErrorJson(msg="密码不合法，请重新输入~~")

        user_info = User.query.filter_by(login_name=login_name).first()
        if not user_info:
            return ops_responseErrorJson(msg="用户名不存在~~")

        # 这里不能重新生成salt，因为MD5是单向散列算法
        if user_info.login_password != UserService.genPwd(login_pwd, user_info.login_salt):
            return ops_responseErrorJson(msg="密码错误~~")

        # 检测用户标志位
        if user_info.status != 1:
            return ops_responseErrorJson(msg="账号已被冻结~~")

        response = make_response(ops_responseJson(msg="登陆成功~~"))
        response.set_cookie(app.config['AUTH_COOKIE_NAME'],
                            '%s#%s' % (UserService.genAuthCode(user_info), user_info.id), 60 * 60 * 24 * 100)

        return response
