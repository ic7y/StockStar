from app import db
from flask import Blueprint, render_template, request, make_response, jsonify, redirect
from common.libs.Helper import *
from common.models.post import Post
from common.libs.DateHelper import *
import uuid
from sqlalchemy.sql import text

post_publish = Blueprint("post_publish_page", __name__, url_prefix="/StockStar")


@post_publish.route("/publish", methods=["GET", "POST"])
def publish():
    if request.method == "GET":
        return render_template("forum.html")
    if request.method == "POST":
        req = request.values

        id = req['id'] if "id" in req else ""
        blogger = req['login_name'] if "login_name" in req else ""
        title = req['title'] if "title" in req else ""
        content = req['content'] if "content" in req else ""
        type = req['option'] if "option" in req else ""
        type_string = req['option_string'] if "option_string" in req else ""
        # picture_url = req['picture_url'] if "picture_url" in req else ""
        status = req['status'] if "status" in req else ""

        uname = uuid.uuid1().hex
        file = request.files.get("file")

        filename = file.filename
        img_name = uname + "-" + filename
        path = "static/files/" + img_name
        try:
            # with open(path, "wb+") as destination:
            file.save(path)
        except Exception as e:
            print('exception: ', e)

        if blogger is None or len(blogger) < 1:
            return ops_responseErrorJson(code=-1, msg="用户名校验失败，请重新登陆~~")
        if title is None or len(title) < 1:
            return ops_responseErrorJson(code=-1, msg="标题太短，少于2个字符~~")
        if content is None or len(content) < 1:
            return ops_responseErrorJson(code=-1, msg="文章太短，少于10个字符~~")
        if status is None or not status.isdigit():
            return ops_responseErrorJson(code=-1, msg="文章发布状态错误，status：0 草稿，1 发布")

        if len(id) > 1 and id.isdigit():
            post = Post.query.filter_by(id=id).first()
            if post is not None:
                if post.blogger != blogger:
                    return ops_responseErrorJson(code=-1, msg="此文章ID，不属于该用户。")
                post.title = title
                post.content = content
                post.picture_uri = path
                post.updated_time = getCurrentTime()
                if post.status == 1 and status == 0:
                    # 文章之前的状态是已发布，当前请求的状态不可为编辑
                    return ops_responseErrorJson(code=-1, msg="文章状态已发布，不可改为编辑。")
            else:
                post = Post()
                post.blogger = blogger
                post.title = title
                post.content = content
                post.type = type
                post.type_string = type_string
                post.status = status
                post.picture_uri = img_name
                post.created_time = getCurrentTime()
                post.updated_time = getCurrentTime()
                db.session.add(post)
        else:
            post = Post()
            post.blogger = blogger
            post.title = title
            post.type = type
            post.type_string = type_string
            post.status = status
            post.content = content
            post.picture_uri = img_name
            post.created_time = getCurrentTime()
            post.updated_time = getCurrentTime()
            db.session.add(post)
        db.session.commit()

        return ops_responseJson(code=200, msg="发布成功！")






