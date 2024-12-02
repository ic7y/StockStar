
from app import db
from common.libs.DateHelper import getOneHourAgo, getCurrentTime, get_now, get_OneDayAgo, get_ThreeMonthsAgo

from common.models import news, stock_index
import tushare as ts


from flask import Blueprint, render_template, request, make_response
from app import *
from common.libs.Helper import *
from common.models.user import *
from common.libs.UserService import *

task_page = Blueprint("task", __name__, url_prefix="/StockStar")




# 获取新闻快讯
def getNews():
    pro = ts.pro_api('509a29c50e178f61e7af4fb7428c6b68c82abf097ba7b3a5228a94cb')

    res = pro.news(src='sina', start_date=getOneHourAgo(), end_date=getCurrentTime())
    news.News.query.delete()
    newsList = []
    for i in range(3):
        newsList.append(news.News(time=res['datetime'][i], content=str(res['content'][i]).ljust(100)[:100]))
    db.session.add_all(newsList)
    db.session.commit()


# 获取股市指数
def getIndex():
    pro = ts.pro_api('509a29c50e178f61e7af4fb7428c6b68c82abf097ba7b3a5228a94cb')
    # 上证指数
    res1 = pro.index_daily(ts_code='000001.SH', start_date=get_ThreeMonthsAgo(), end_date=get_now())
    # 深圳成指
    res2 = pro.index_daily(ts_code='399001.SZ', start_date=get_ThreeMonthsAgo(), end_date=get_now())
    # 创业板
    res3 = pro.index_daily(ts_code='399006.SZ', start_date=get_ThreeMonthsAgo(), end_date=get_now())
    # 中小板
    res4 = pro.index_daily(ts_code='399005.SZ', start_date=get_ThreeMonthsAgo(), end_date=get_now())

    stock_index.StockIndex.query.delete()

    for i in range(len(res1) - 1):
        index = stock_index.StockIndex()
        index.code = res1['ts_code'][i]
        index.time = res1['trade_date'][i]
        index.open = res1['open'][i]
        index.close = res1['close'][i]
        index.highest = res1['high'][i]
        index.lowest = res1['low'][i]
        db.session.add(index)

    for i in range(len(res2) - 1):
        index = stock_index.StockIndex()
        index.code = res2['ts_code'][i]
        index.time = res2['trade_date'][i]
        index.open = res2['open'][i]
        index.close = res2['close'][i]
        index.highest = res2['high'][i]
        index.lowest = res2['low'][i]
        db.session.add(index)

    for i in range(len(res3) - 1):
        index = stock_index.StockIndex()
        index.code = res3['ts_code'][i]
        index.time = res3['trade_date'][i]
        index.open = res3['open'][i]
        index.close = res3['close'][i]
        index.highest = res3['high'][i]
        index.lowest = res3['low'][i]
        db.session.add(index)

    for i in range(len(res4) - 1):
        index = stock_index.StockIndex()
        index.code = res4['ts_code'][i]
        index.time = res4['trade_date'][i]
        index.open = res4['open'][i]
        index.close = res4['close'][i]
        index.highest = res4['high'][i]
        index.lowest = res4['low'][i]
        db.session.add(index)

    db.session.commit()



@task_page.route("/task", methods=["GET", "POST"])
def task():
    print("start get news.")
    getNews()
    print("start get stock.")
    getIndex()
    print("finish to get news and stock.")
