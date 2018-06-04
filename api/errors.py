from flask import jsonify, make_response
from . import api

errors = {
    'ResourceNotFound': {
        'message': 'not found',
        'ststus': 404
    }
}

api.errors = errors