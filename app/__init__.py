#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# create app
app = Flask(__name__)
app.config.from_object('config')

# create instance of LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

# create db connection
db = SQLAlchemy(app)

# register blueprints
from app.dashboard.views import mod as mod_dashboard
app.register_blueprint(mod_dashboard)

from app.login.views import mod as mod_login
app.register_blueprint(mod_login)

from app.logout.views import mod as mod_logout
app.register_blueprint(mod_logout)

from app.index.views import mod as mod_index
app.register_blueprint(mod_index)

from app.animal.views import mod as mod_animals
app.register_blueprint(mod_animals)

from app.doc.views import mod as mod_docs
app.register_blueprint(mod_docs)

from app.event.views import mod as mod_events
app.register_blueprint(mod_events)

from app.register.views import mod as mod_register
app.register_blueprint(mod_register)

from app.privacy.views import mod as mod_privacy
app.register_blueprint(mod_privacy)
