# coding: utf-8
from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, info='用户ID')
    login_name = db.Column(db.String(20, 'utf8mb4_general_ci'), nullable=False, unique=True, info='用户名')
    login_password = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, info='密码')
    login_salt = db.Column(db.String(32, 'utf8mb4_general_ci'), nullable=False, info='盐值')
    status = db.Column(db.Integer, nullable=False, server_default=db.FetchedValue(), info='用户状态位')
    updated_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='更新时间')
    created_time = db.Column(db.DateTime, nullable=False, server_default=db.FetchedValue(), info='创建时间')
