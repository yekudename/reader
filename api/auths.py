import jwt, datetime, time
from flask import jsonify, request
from models import User
import config
from . import common

class Auth():
    @staticmethod
    def encode_auth_token(user_id, login_time):
        """
        生产认证Token
        :param user_id: int
        :param login_time: int(timestamp)
        :return: string
        """
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                config.Config.SECRET_KEY,
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        """
        验证Token
        :param auth_token:
        :return: string|integer
        """
        try:
            # payload = jwt.decode(auth_token, config.Config.SECRET_KEY, options={'verify_exp': False})
            payload = jwt.decode(auth_token, config.Config.SECRET_KEY)
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token已过期'
        except jwt.InvalidTokenError:
            return '无效的Token'

    def authenticate(self, username, password):
        """
        用户登录， 登录成功返回token， 将登录时间写入数据库
        :return: json
        """
        user_info = User.query.filter_by(nick_name=username).first()
        if user_info is None:
            return jsonify(common.false_return('', '找不到用户'))
        else:
            if user_info.verify_password(password):
                user_info.login_time = int(time.time())
                token = self.encode_auth_token(user_info.id, user_info.login_time)
                return jsonify(common.true_return(token.decode(), '登录成功'))
            else:
                return jsonify(common.false_return('', '密码不正确'))

    def identity(self, payload):
        """
        用户鉴权
        :return: list
        """
        auth_header = request.headers.get('Authorization')
        if auth_header:
            auth_token_arr = auth_header.split(' ')
            if not auth_token_arr or auth_token_arr[0] != 'JWT' or len(auth_token_arr) != 2:
                result = common.false_return('', '请传入正确的验证头信息')
            else:
                auth_token = auth_token_arr[1]
                payload = self.decode_auth_token(auth_token)
                if not isinstance(payload, str):
                    user = User.query.filter_by(id=payload['data']['id']).first()
                    if user is None:
                        result = common.false_return('', '找不到用户')
                    else:
                        if user.login_time == payload['data']['login_time']:
                            result = common.true_return(user.to_json(), '请求成功')
                        else:
                            result = common.false_return('', 'Token已更改，请重新登录')
                else:
                    result = common.false_return('', payload)
        else:
            result = common.false_return('', 'token为空')
        return result