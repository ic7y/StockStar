from flask import Flask

from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:991022@127.0.0.1/stockstar"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_ENCODING'] = "utf8mb4"
app.config['SECRET_KEY'] = "flask_2021"

# 设置app Cookie的KEY字段
app.config['AUTH_COOKIE_NAME'] = "StockStar"
# 防止debugTool拦截redirect请求
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False


class SchedulerConfig(object):
    JOBS = [
        {
            'id': '1',  # 任务id
            'func': 'controllers.task:getNews',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'interval',  # 任务执行类型，定时器
            'minutes': 60,  # 任务执行时间，单位分
        },
        {
            'id': '2',  # 任务id
            'func': 'controllers.task:getIndex',  # 任务执行程序
            'args': None,  # 执行程序参数
            'trigger': 'interval',  # 任务执行类型，定时器
            'minutes': 720,  # 任务执行时间，单位分
        }
    ]
    SCHEDULER_API_ENABLED = True
    SCHEDULER_TIMEZONE = 'Asia/Shanghai'  # 给定时器指定时区，防止warning


app.config.from_object(SchedulerConfig())

db = SQLAlchemy(app)
