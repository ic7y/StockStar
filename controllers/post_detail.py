from flask import Blueprint, render_template, g, request, make_response, redirect

from common.libs.DateHelper import getCurrentTime
from common.libs.Helper import ops_render, ops_responseJson, ops_responseErrorJson
from common.models.post import *
from common.models.comment import *
from common.models.user import *

detail_page = Blueprint("detail_page", __name__, url_prefix="/StockStar/post")


@detail_page.route("/detail/<blog_id>", methods=["GET", "POST"])
def detail(blog_id):
    if request.method == "POST" and "comment" not in request.form:
        req = request.values
        id = req['id'] if "id" in req else ""

        if not id.isdigit():
            return ops_responseErrorJson(code=-1, msg="blog ID error!")

        post = (Post.query.filter_by(id=int(id)).first())
        if post is not None:
            return make_response(ops_responseJson(msg="request success!"))
        return make_response(ops_responseErrorJson(code=-1, msg="request failure~~"))
    if request.method == "POST" and "comment" in request.form:
        comment = request.form["comment"]
        url = "/StockStar/post/detail/" + blog_id
        if comment is "":
            return make_response(redirect(url))
        newComment = Comment()
        newComment.comment_content = comment
        newComment.created_time = getCurrentTime()
        newComment.post_id = blog_id
        newComment.comment_publisher = g.current_user.login_name
        db.session.add(newComment)
        db.session.commit()
        return make_response(redirect(url))

    if request.method == "GET":
        id = blog_id
        if id is not None and id.isdigit():
            post = Post.query.filter_by(id=int(id)).first()
            comment = Comment.query.filter_by(post_id=int(id))

            context = {'data': post, 'comment': comment}
            return ops_render("post_detail.html", context)
        return make_response(ops_responseErrorJson(code=-1, msg="post not Found!"))
