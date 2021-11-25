import datetime


def getCurrentTime():
    fmt = "%Y-%m-%d %H:%M:%S"
    now = datetime.datetime.now()
    return now.strftime(fmt)


def getOneHourAgo():
    fmt = "%Y-%m-%d %H:%M:%S"
    oneHourAgo = datetime.datetime.now() - datetime.timedelta(minutes=60)
    return oneHourAgo.strftime(fmt)


def get_now():
    now = datetime.datetime.now()
    fmt = "%Y%m%d"
    return now.strftime(fmt)


def get_OneDayAgo():
    fmt = "%Y%m%d"
    oneHourAgo = datetime.datetime.now() - datetime.timedelta(hours=24)
    return oneHourAgo.strftime(fmt)


def get_ThreeMonthsAgo():
    fmt = "%Y%m%d"
    threeMonthsAgo = datetime.datetime.now() - datetime.timedelta(days=90)
    return threeMonthsAgo.strftime(fmt)
