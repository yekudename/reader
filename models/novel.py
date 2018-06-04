from datetime import datetime
import enum
import json
from flask import jsonify
from sqlalchemy.orm import backref

from .utils import DateTimeEncoder, get_count

from ext import db

class NovelState(enum.Enum):
    start = 0
    middle = 1
    end = 2

def get_state(state = None):
    if state == NovelState.start or state == NovelState.middle:
        return "连载"
    elif state == NovelState.end:
        return "完结"
    else:
        return None

class NovelInfo(db.Model):
    __tablename__ = 'novel_info'
    __table_args__ = {'mysql_charset': 'utf8mb4'}

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(100), default='')
    name = db.Column(db.String(60), default='')
    author = db.Column(db.String(30), default='')
    description = db.Column(db.Text, default='')
    category = db.Column(db.String(20), default='')
    last_chapter = db.Column(db.String(30), default='')
    keywords = db.Column(db.String(60), default='')
    word_count = db.Column(db.Integer, default=0)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow)
    img = db.Column(db.String(255), default='')
    state = db.Column(db.Enum(NovelState), default=NovelState.start)
    chapters = db.relationship('NovelChapter', backref='novel_info')

    def to_json(self):
        novel_json = {
            'id': self.id,
            'url': self.url,
            'name': self.name,
            'author': self.author,
            'category': self.category,
            'description': self.description,
            'last_chapter': self.last_chapter,
            'keywords': self.keywords,
            'word_count': get_count(self.word_count),
            'img': self.img,
            'updatetime': json.dumps(self.updatetime, cls=DateTimeEncoder),
            'state': get_state(self.state),
            'chapters': [c.to_json() for c in self.chapters]
        }

        return novel_json

class NovelChapter(db.Model):
    __tablename__ = 'novel_chapter'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), default='')
    word_count = db.Column(db.Integer, default=0)
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow)
    novel_info_id = db.Column(db.Integer, db.ForeignKey('novel_info.id'))
    chapter_detail = db.relationship('NovelChapterDetail',backref=backref('novel_chapter',uselist=False))

    def to_json(self):
        chapter_json = {
            'id': self.id,
            'title': self.title,
            'updatetime': json.dumps(self.updatetime, cls=DateTimeEncoder)
        }

        return chapter_json

class NovelChapterDetail(db.Model):
    __tablename__ = 'novel_chapter_detail'
    __table_args__ = {'mysql_charset': 'utf8mb4'}
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), default='')
    word_count = db.Column(db.Integer, default=0)
    text = db.Column(db.Text, default='')
    createtime = db.Column(db.DateTime, default=datetime.utcnow)
    updatetime = db.Column(db.DateTime, default=datetime.utcnow)
    chapter_id = db.Column(db.Integer, db.ForeignKey('novel_chapter.id'))

    def to_json(self):
        chapter_detail_json = {
            'id': self.id,
            'title': self.novel_chapter.title,
            'text': '&emsp;&emsp;' + self.text.replace('\n','<br/><br/>&emsp;&emsp;'),
            'updatetime': json.dumps(self.updatetime, cls=DateTimeEncoder)
        }

        return chapter_detail_json
