#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========================================
# @Author		=   xefvan
# @Version		=   1.0
# @DateTime     =   2017-08-01 22:50:48
# ========================================

import os

from flask import Flask
from flask_script import Server, Shell, Manager, Command, prompt_bool

from app import create_app
from app.extensions import db

manager = Manager(create_app('config.py'))

manager.add_command("runserver", Server('0.0.0.0',port=8080))

def make_shell_context():
	return dict(db=db)

manager.add_command("shell", Shell(make_context=make_shell_context))

@manager.command
def createall():
	"""Create all database tables"""
	db.create_all()

@manager.command
def dropall():
	"""Drop all database tables"""
	if prompt_bool("Are you sure ? You will lose all your database tables!"):
		db.drop_all()

if __name__ == '__main__':
	manager.run()