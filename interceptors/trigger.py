from app import *


# 第一次请求后端的时候触发获取新闻的定时器
@app.before_first_request
def trigger_getNews():
    from controllers.task import getNews
    getNews()


# 第一次请求后端的时候触发获取股市指数的定时器
@app.before_first_request
def trigger_getIndex():
    from controllers.task import getIndex
    getIndex()
