from flask import jsonify, g, render_template


# 返回AJAX POST成功的json数据
def ops_responseJson(code=200, msg="操作成功~~", data=None):
    if data is None:
        data = {}
    res = {"code": code, "msg": msg, "data": data}
    return jsonify(res)


# 返回AJAX POST失败的json数据
def ops_responseErrorJson(code=-1, msg="操作失败~~", data=None):
    if data is None:
        data = {}
    res = {"code": code, "msg": msg, "data": data}
    return jsonify(res)


# 自定义渲染用户状态到页面的方法
def ops_render(template, context=None):
    if context is None:
        context = {}
    if 'current_user' in g:
        context['current_user'] = g.current_user

    return render_template(template, **context)
