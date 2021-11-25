import os
import sys
import traceback

from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

from www import *
from flask_script import Server, Command
from flask_script import Manager

scheduler = APScheduler(scheduler=BackgroundScheduler())
scheduler.init_app(app)
scheduler.start()

manager = Manager(app)
# 添加服务器启动命令
manager.add_command("runserver", Server("127.0.0.1", use_debugger=True, use_reloader=False))


# 添加数据表创建命令
@Command
def create_all():
    db.create_all()


manager.add_command("db_init", create_all)

if __name__ == "__main__":
    try:
        manager.run()
    except Exception as e:
        traceback.print_exc()
