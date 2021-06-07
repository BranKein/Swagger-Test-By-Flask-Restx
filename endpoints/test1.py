from flask import Blueprint
from flask_restx import Namespace, Resource, reqparse
from . import is_api, cors_allow

test1_app = Blueprint('test1', __name__, url_prefix='/test1')
test1_api = Namespace('test1', path='/test1')


@test1_api.route('/resource1')
class FirstResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('num', type=int, default=1, help='페이지 번호')

    @test1_api.expect(parser)
    @test1_api.response(200, 'Success')
    @test1_api.response(403, 'No Permission')
    @is_api(required_keys=['num'])
    def get(self, data):
        print(data)
        result = {'success': data['num']}
        return result, 200

    @test1_api.hide
    @cors_allow('http://127.0.0.1:5000')
    def options(self):
        pass
