#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========================================
# @Author		=   xefvan
# @Version		=   1.0
# @DateTime     =   2017-08-01 23:06:55
# ========================================

from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
api = Api()