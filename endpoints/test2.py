from flask import Blueprint
from flask_restx import Namespace, Resource, reqparse, Api
from . import is_api

test2_app = Blueprint('test2', __name__, url_prefix='/test2')
test2_api = Namespace('test2', path='/test2')


