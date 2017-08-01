#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# ========================================
# @Author		=   xefvan
# @Version		=   1.0
# @DateTime     =   2017-08-01 22:59:55
# ========================================

import os
import logging
import datetime

from logging.handlers import SMTPHandler, RotatingFileHandler

from flask import Flask, g, session, request, flash, redirect, jsonify, url_for

from .extensions import db, api

DEFAULT_APP_NAME = 'MyWeb'

DEFAULT_MODULES = (

)

def create_app(config=None):

	app = Flask(DEFAULT_APP_NAME)

	# config
	app.config.from_pyfile(config)

	configure_extensions(app)
	configure_logggin(app)

	return app


def configure_extensions(app):
	# configure extensions
	db.init_app(app)
	api.init_app(app)


def configure_logggin(app):
	# format
	formatter = logging.Formatter(
		'%(asctime)s %(levelname)s: %(message)s '
		'[in %(pathname)s:%(lineno)d]')

	# debug log
	debug_log = os.path.join(app.root_path,
							 app.config['DEBUG_LOG'])

	debug_file_handler = \
		RotatingFileHandler(debug_log,
							maxBytes=100000,
							backupCount=10)

	debug_file_handler.setLevel(logging.DEBUG)
	debug_file_handler.setFormatter(formatter)
	app.logger.addHandler(debug_file_handler)

	# error log
	error_log = os.path.join(app.root_path, 
							 app.config['ERROR_LOG'])

	error_file_handler = \
		RotatingFileHandler(debug_log,
							maxBytes=100000,
							backupCount=10)

	error_file_handler.setLevel(logging.ERROR)
	error_file_handler.setFormatter(formatter)
	app.logger.addHandler(error_file_handler)