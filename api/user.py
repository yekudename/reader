# -*- coding:utf-8 -*-

from flask import jsonify, request, current_app, url_for, abort, g, make_response
from flask_restful import reqparse, Resource, fields, marshal_with

from . import api
from models.user import User, Group
from ext import db
from . import common
from api.auths import Auth

class UserApi(Resource):

    def __init__(self):
        self.get_reqparse = reqparse.RequestParser()
        self.post_reqparse = reqparse.RequestParser()
        self.put_reqparse = reqparse.RequestParser()
        self.delete_reqparse = reqparse.RequestParser()

        self.get_reqparse.add_argument('page', type = int, location = ['json', 'args', 'headers'], required = False)
        
        self.post_reqparse.add_argument('nickname', type = str, location = ['json', 'args'], required = True)
        self.post_reqparse.add_argument('password', type = str, location = ['json', 'args'], required = True)
        
        self.put_reqparse.add_argument('nick_name', type = str)
        self.put_reqparse.add_argument('sex', type = int, default = 1)
        self.put_reqparse.add_argument('email', type = str)
        self.put_reqparse.add_argument('province', type = str)
        self.put_reqparse.add_argument('city', type = str)
        self.put_reqparse.add_argument('sigature', type = str)

        super(UserApi, self).__init__()

    def get(self):
        result = Auth.identity(Auth, request)
        if result['status'] and result['data']:
            return result['data']
        else:
            return result
            # args = self.get_reqparse.parse_args()
            # page = args['page'] or 1

            # pagination = User.query.paginate(
            #     page, per_page=current_app.config['USERS_PER_PAGE'],
            #     error_out=False
            # )

            # users = pagination.items
            # _prev = None
            # if pagination.has_prev:
            #     _prev = url_for('api.api_user', page=page-1, _external=True)
            # _next = None
            # if pagination.has_next:
            #     _next = url_for('api.api_user', page=page+1, _external=True)
            # return {
            #     'users': [user.to_json() for user in users],
            #     'prev': _prev,
            #     'next': _next,
            #     'count': pagination.total
            # }

    def post(self):
        args = self.post_reqparse.parse_args(strict=True)
        nickname = args['nickname']
        pwd = args['password']
        if nickname is None or pwd is None:
            abort(400)

        user = User.query.filter_by(nick_name=nickname).first()
        if user is not None:
            return jsonify(common.false_return('', '用户名已存在'))
        else:
            new_user = User()
            new_user.hash_password(pwd)
            new_user.nick_name = nickname

            db.session.add(new_user)
            db.session.commit()

            return_user = {
                'id': new_user.id,
                'nickname': new_user.nick_name,
                'login_count': new_user.login_count
            }
            return jsonify(common.true_return(return_user, '用户注册成功'))

    def put(self, user_id = None):
        if not user_id:
            abort(400)
        
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404)

        args = self.put_reqparse.parse_args()
        if args['sex']:
            user.sex = args['sex']
        if args['nick_name']:
            user.nick_name = args['nick_name']
        if args['email']:
            user.email = args['email']
        if args['city']:
            user.city = args['city']
        if args['province']:
            user.province = args['province']
        if args['sigature']:
            user.sigature = args['sigature']

        db.session.add(user)
        db.session.commit()

        return (user.id, 201)

    def delete(self, user_id = None):
        if not user_id:
            abort(400)
        
        user = User.query.filter_by(id=user_id).first()
        if not user:
            abort(404)
        
        db.session.delete(user)
        db.session.commit()

class LoginApi(Resource):
    def __init__(self):
        self.post_reqparse = reqparse.RequestParser()
        
        self.post_reqparse.add_argument('nickname', type = str, location = ['json', 'args'], required = True)
        self.post_reqparse.add_argument('password', type = str, location = ['json', 'args'], required = True)

        super(LoginApi, self).__init__()

    def post(self):
        args = self.post_reqparse.parse_args(strict=True)
        nickname = args['nickname']
        pwd = args['password']
        if nickname is None or pwd is None:
            return jsonify(common.false_return('', '用户名或密码为空'))
        else:
            return Auth.authenticate(Auth, nickname, pwd)

    def delete(self):
        result = Auth.identity(Auth, request)
        if result['status'] and result['data']:
            user = User.query.filter_by(id=result['data']['id']).first()
            user.login_time = None
            return jsonify(common.true_return(user.id, '退出成功'))
        else:
            return jsonify(common.false_return('', '退出失败'))

api.add_resource(UserApi, '/user', endpoint = 'api_user')
api.add_resource(LoginApi, '/login', endpoint = 'api_login')