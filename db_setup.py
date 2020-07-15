#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
from app import db
from app.user.models import User
from app.animal.model import Animal
from app.doc.model import Doc
from app.event.model import Event

if __name__ == '__main__':
    db.create_all()
