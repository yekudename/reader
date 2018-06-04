# -*- coding:utf-8 -*-

from sqlalchemy.ext.hybrid import hybrid_method, hybrid_property
from sqlalchemy.exc import SQLAlchemyError
from flask import url_for
from passlib.apps import custom_app_context as pwd_context
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

from ext import db
import app

roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)

group_relationship = db.Table(
    'group_relationship',
    db.Column('group_id', db.Integer, db.ForeignKey('user_groups.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    mysql_charset='utf8mb4'
)

friendship = db.Table(
    'friends',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('friend_id', db.Integer, db.ForeignKey('users.id')),
    mysql_charset='utf8mb4'
)

mp_relationship = db.Table(
    'mp_relationship',
    db.Column('mp_id', db.Integer, db.ForeignKey('mps.id'), nullable=False),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), nullable=False),
    mysql_charset='utf8mb4'
)

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(255))

    def __repr__(self):
        return '<Role %s>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    sex = db.Column(db.SmallInteger, default=2)
    nick_name = db.Column(db.String(60), index=True)
    password = db.Column(db.String(255))
    phone = db.Column(db.String(20))
    email = db.Column(db.String(40))
    signature = db.Column(db.String(512), default='')
    province = db.Column(db.String(20), default='')
    city = db.Column(db.String(20), default='')
    active = db.Column(db.Boolean())
    login_time = db.Column(db.Integer)
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(63))
    current_login_ip = db.Column(db.String(63))
    login_count = db.Column(db.Integer)
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users'))#, lazy='dynamic'))
    groups = db.relationship('Group', secondary=group_relationship, backref='members')
    mps = db.relationship('MP', secondary=mp_relationship, backref='users')
    friends = db.relationship('User',
                              secondary=friendship,
                              primaryjoin=(friendship.c.user_id == id),
                              secondaryjoin=(friendship.c.friend_id == id),
                              lazy='dynamic')
    
    def __repr__(self):
        return '<User %r>' % self.nick_name

    def to_json(self):
        json_user = {
            'id': self.id,
            'nickname': self.nick_name,
            'phone': self.phone,
            'email': self.email,
            'signature': self.signature,
            'province': self.province,
            'signature': self.signature,
            'city': self.city
        }
        return json_user

    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)

    def generate_auth_token(self, expiration = 600):
        s = Serializer(app.app.config['SECRET_KEY'], expires_in=expiration)
        return s.dumps({'id':self.id})

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def update(self):
        return session_commit()

    @staticmethod
    def verify_auth_token(token):
        s = Serializer(app.app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except SignatureExpired:
            return None   # valid token, but expired
        except BadSignature:
            return None   # invalid token
        user = User.query.get(data['id'])
        return user

    @hybrid_method
    def add_friend(self, user):
        if not self.is_friend(user):
            self.friends.append(user)
            user.friends.append(self)
            return self

    @hybrid_method
    def del_friend(self, user):
        if self.is_friend(user):
            self.friends.remove(user)
            user.friends.remove(self)
            return self

    @hybrid_method
    def is_friend(self, user):
        return self.friends.filter(friendship.c.friend_id == user.id).count() > 0

    @hybrid_method
    def add_group(self, group):
        if not self.is_in_group(group):
            self.groups.append(group)

    @hybrid_method
    def del_group(self, group):
        if self.is_in_group(group):
            self.groups.remove(group)

    @hybrid_method
    def is_in_group(self, group):
        return group in self.groups

class Group(db.Model):
    __tablename__ = 'user_groups'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    owner_id = db.Column(db.Integer, index=True)
    nick_name = db.Column(db.String(60), index=True)

    def __repr__(self):
        return '<Group %r>' % self.nick_name

    @hybrid_method
    def is_member(self, user):
        return user in self.members

class MP(db.Model):
    __tablename__ = 'mps'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(20), default='')
    province = db.Column(db.String(20), default='')
    nick_name = db.Column(db.String(60), index=True)
    signature = db.Column(db.String(255), default='')

    def __repr__(self):
        return '<MP %r>' % self.nick_name


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
