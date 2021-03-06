#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask_login import UserMixin
from passlib.apps import custom_app_context as pwd_context
from app import db, login_manager


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
