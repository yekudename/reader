import os
from flask import Flask, Blueprint, session, current_app
from flask_restful import Api, Resource
from flask_sqlalchemy import get_debug_queries
from flask_cors import CORS

import config

api_bp = Blueprint('api', __name__, url_prefix = '/api')
#CORS(api_bp, supports_credentials=True)

api = Api(api_bp)

# @api_bp.after_request
# def add_header(response):
#     response.headers.add('Access-Control-Allow-Origin', '*')
#     response.headers.add('Access-Control-Allow-Credentials', True)
#     response.headers.add(
#         'Access-Control-Allow-Headers', 'Content-Type, Authorization, x-requested-with')
#     response.headers.add(
#         'Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
#     return response

#一定要导入
from . import user, novel