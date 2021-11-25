
from controllers.index import *
from controllers.login import *
from controllers.register import *
from controllers.logout import *
from controllers.forum import *
from controllers.post_publish import *
from controllers.post_detail import *
from controllers.personal_page import *
from controllers.get_index_api import *


from flask_debugtoolbar import DebugToolbarExtension

app.debug = True
toolbar = DebugToolbarExtension(app)

# 错误处理器和拦截器
from interceptors.trigger import *
from interceptors.Auth import *
from interceptors.errorHandler import *

# 注册蓝图
app.register_blueprint(index_page)
app.register_blueprint(login_page)
app.register_blueprint(register_page)
app.register_blueprint(logout_page)
app.register_blueprint(forum_page)
app.register_blueprint(post_publish)
app.register_blueprint(detail_page)
app.register_blueprint(personal_page)
app.register_blueprint(get_index_api_page)


