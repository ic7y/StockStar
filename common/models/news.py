# coding: utf-8
from app import db


class News(db.Model):
    __tablename__ = 'news'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text(collation='utf8mb4_general_ci'), nullable=False)
    time = db.Column(db.DateTime, nullable=False)
