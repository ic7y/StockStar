from app import db


class Post(db.Model):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True, info='帖子ID')
    blogger = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, info='发帖人用户名')
    title = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, info='帖子名称')
    content = db.Column(db.Text(5000,'utf8mb4_general_ci'), nullable=False, info='帖子内容地址')
    type = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, info='主题')
    type_string = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, info='主题_String')
    picture_uri = db.Column(db.String(128, 'utf8mb4_general_ci'), nullable=False, info='图片地址')
    status = db.Column(db.Integer, nullable=False, default=0, server_default='0', info='发帖状态：0：草稿、1：已发布 default：0')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
