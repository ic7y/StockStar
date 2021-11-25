from app import db
from common.libs.DateHelper import getOneHourAgo, getCurrentTime, get_now, get_OneDayAgo, get_ThreeMonthsAgo

from common.models import news, stock_index
import tushare as ts


# 获取新闻快讯
def getNews():
    pro = ts.pro_api('ecbdabe501310ab88ec39a98934b767ad04f9954cf1049c73a1acacd')

    res = pro.news(src='sina', start_date=getOneHourAgo(), end_date=getCurrentTime())
    news.News.query.delete()
    newsList = []
    for i in range(3):
        newsList.append(news.News(time=res['datetime'][i], content=str(res['content'][i]).ljust(100)[:100]))
    db.session.add_all(newsList)
    db.session.commit()


# 获取股市指数
def getIndex():
    pro = ts.pro_api('ecbdabe501310ab88ec39a98934b767ad04f9954cf1049c73a1acacd')
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



