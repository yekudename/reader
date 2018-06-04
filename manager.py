# -*- coding=utf-8 -*-
import os
import click
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from ext import db
from models import *
from models.novel import NovelState
from flask_security.utils import encrypt_password

COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()

if os.path.exists('.env'):
    print('Importing environment from .env...')
    for line in open('.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1]


db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def deploy():
    """Run deployment tasks."""
    from flask_migrate import init, migrate, upgrade

    # migrate database to latest revision
    try: init()
    except: pass
    migrate()
    upgrade()

@manager.command
def dropall():
    db.drop_all()
    print("all tables dropped! remember to delete directory: migrations")

@manager.command
def initrole():
    db.session.add(Role(name="superuser"))
    db.session.add(Role(name="admin"))
    db.session.add(Role(name="editor"))
    db.session.add(Role(name="author"))
    db.session.add(Role(name="user"))
    pwd = os.getenv('FLASK_ADMIN_PWD') or input("Pls input Flask admin pwd:")
    new_user = User()
    new_user.email = "user"
    new_user.password = encrypt_password(pwd)
    new_user.active = True
    db.session.add(new_user)
    # Heroku postgres ������commit�����������roles_users��ϵ
    db.session.commit()
    ins=roles_users.insert().values(user_id="2", role_id="5")
    db.session.execute(ins)
    db.session.commit()
    print("Roles added!")

@manager.command
def adduser():
    pwd = os.getenv('FLASK_ADMIN_PWD') or input("Pls input Flask admin pwd:")
    new_user = User()
    new_user.email = "user"
    new_user.password = encrypt_password(pwd)
    new_user.active = True
    db.session.add(new_user)
    # Heroku postgres ������commit�����������roles_users��ϵ
    db.session.commit()
    ins=roles_users.insert().values(user_id="2", role_id="5")
    db.session.execute(ins)
    db.session.commit()
    print("Roles added!")


@manager.option('-f', '--file', dest='file', help='file path', default='(章节)大劫主.txt')
def insert_novel_to_db(file):
    novel = NovelInfo(name="天生就会跑",author="丧尸舞",description="从踏上跑道的那一天，我才发现，原来，人生有另一种选择！",category="游戏",word_count=76114,img='/static/img/book10009.jpg',updatetime='2018-05-17 10:49:29')
    with open(file, 'r', encoding='utf-8') as f:

        lines = f.readlines()
        index = 1
        for line in lines:
            l = line.strip()
            if l:
                chapter = NovelChapter(title=l)
                path = str(index) + file
                index += 1
                with open(path, 'r', encoding='utf-8') as f1:
                    detail = NovelChapterDetail(text=f1.read(),novel_chapter=chapter)
                novel.chapters.append(chapter)
                db.session.add(novel)
                db.session.commit()
            else:
                break

@manager.command
def update_table():
    query = db.session.query
    t = query(NovelInfo).filter_by(id=1).first()
    t.state = NovelState.start
    db.session.add(t)
    db.session.commit()

if __name__ == '__main__':
    manager.run()
