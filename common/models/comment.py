from app import db


class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, info='评论ID')
    post_id = db.Column(db.Integer, nullable=False, info='帖子ID')
    comment_publisher = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, info='评论人')
    comment_content = db.Column(db.Text(100,'utf8mb4_general_ci'), nullable=False, info='评论内容')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')