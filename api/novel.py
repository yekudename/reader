# -*- coding:utf-8 -*-

from flask import jsonify, request, current_app, url_for, abort
from flask_restful import reqparse, Resource, fields, marshal_with

from . import api
from models.novel import NovelInfo, NovelChapter, NovelChapterDetail
from ext import db

class NovelApi(Resource):

    def __init__(self):
        self.get_reqparse = reqparse.RequestParser()
        self.post_reqparse = reqparse.RequestParser()
        self.put_reqparse = reqparse.RequestParser()
        self.delete_reqparse = reqparse.RequestParser()

        self.get_reqparse.add_argument('page', type = int, location = ['json', 'args', 'headers'], required = False)
        
        self.post_reqparse.add_argument('phone', type = str, location = ['json', 'args'], required = True)
        self.post_reqparse.add_argument('password', type = str, location = ['json', 'args'], required = True)
        
        self.put_reqparse.add_argument('nick_name', type = str)
        self.put_reqparse.add_argument('sex', type = int, default = 1)
        self.put_reqparse.add_argument('email', type = str)
        self.put_reqparse.add_argument('province', type = str)
        self.put_reqparse.add_argument('city', type = str)
        self.put_reqparse.add_argument('sigature', type = str)

        super(NovelApi, self).__init__()

    def get(self, novel_id = None):
        if novel_id:
            novel = NovelInfo.query.filter_by(id=novel_id).first()
            if not novel:
                abort(404)
            return novel.to_json()
        else:
            args = self.get_reqparse.parse_args()
            page = args['page'] or 1

            pagination = NovelInfo.query.paginate(
                page, per_page=current_app.config['NOVELS_PER_PAGE'],
                error_out=False
            )

            novels = pagination.items
            if not novels:
                abort(404)
            _prev = None
            if pagination.has_prev:
                _prev = url_for('api.userlistapi', page=page-1, _external=True)
            _next = None
            if pagination.has_next:
                _next = url_for('api.userlistapi', page=page+1, _external=True)
            return {
                'novels': [novel.to_json() for novel in novels],
                'prev': _prev,
                'next': _next,
                'count': pagination.total
            }

    def post(self, novel_id = None):
        if novel_id:
            abort(400)
        else:
            args = self.post_reqparse.parse_args(strict=True)

            novel = NovelInfo.query.filter_by(name=args['name']).first()
            if novel:
                abort(300)
            else:
                new_novel = NovelInfo()
                new_novel.password = args['password']
                new_novel.phone = args['phone']

                db.session.add(new_novel)
                db.session.commit()

                return (new_novel.id, 201)

    def put(self, novel_id = None):
        if not novel_id:
            abort(400)
        
        novel = NovelInfo.query.filter_by(id=novel_id).first()
        if not novel:
            abort(404)

        args = self.put_reqparse.parse_args()
        if args['name']:
            novel.name = args['name']

        db.session.add(novel)
        db.session.commit()

        return (novel.id, 201)

    def delete(self, novel_id = None):
        if not novel_id:
            abort(400)
        
        novel = NovelInfo.query.filter_by(id=novel_id).first()
        if not novel:
            abort(404)
        
        db.session.delete(novel)
        db.session.commit()

class NovelChapterApi(Resource):
    def __init__(self):
        self.get_reqparse = reqparse.RequestParser()

        self.get_reqparse.add_argument('page', type = int, location = ['json', 'args', 'headers'], required = False)

    def get(self, novel_id = None):
        if novel_id:
            novel = NovelInfo.query.filter_by(id=novel_id).first()
            if not novel:
                abort(404)
            return {
                'novel_id': novel.id,
                'chapters': [c.to_json() for c in novel.chapters]
            }
        else:
            abort(404)

class NovelChapterDetailApi(Resource):
    
    def get(self, chapter_id = None):
        if chapter_id:
            chapter_detail = NovelChapterDetail.query.filter_by(chapter_id=chapter_id).first()
            if not chapter_detail:
                abort(404)
            return {
                'chapter_detail': chapter_detail.to_json()
            }
        else:
            abort(404)

class SearchApi(Resource):
    def __init__(self):
        self.get_reqparse = reqparse.RequestParser()

        self.get_reqparse.add_argument('query', type = str, location = ['json', 'args', 'headers'], required = True)
        self.get_reqparse.add_argument('page', type = int, location = ['json', 'args', 'headers'], required = False)
        self.get_reqparse.add_argument('perpage', type = int, location = ['json', 'args', 'headers'], required = False)

        super(SearchApi, self).__init__()

    def get(self):
        args = self.get_reqparse.parse_args()
        query = args['query']
        page = args['page'] or 1
        perpage = args['perpage'] or current_app.config['NOVELS_PER_PAGE']

        if query is "":
          return {
            'novels': [],
            'count': None,
            'prev': None,
            'next': None
          }

        pagination = NovelInfo.query.filter(NovelInfo.name.ilike('%' + query + '%')).paginate(page, per_page = perpage, error_out = False)

        novels = pagination.items
        _prev = None
        if pagination.has_prev:
            _prev = url_for('api.api_search', query=query, page=page-1, perpage=perpage, _external=True)
        _next = None
        if pagination.has_next:
            _next = url_for('api.api_search', query=query, page=page+1, perpage=perpage, _external=True)

        return {
            'novels': [novel.to_json() for novel in novels],
            'count': pagination.total,
            'prev': _prev,
            'next': _next
        }

api.add_resource(NovelApi, '/novel', '/novel/<int:novel_id>', endpoint = 'api_novel')
api.add_resource(NovelChapterApi, '/chapter/<int:novel_id>', endpoint ='api_chapter')
api.add_resource(NovelChapterDetailApi, '/chapter_detail/<int:chapter_id>', endpoint ='api_chapter_detail')
api.add_resource(SearchApi, '/search', endpoint='api_search')