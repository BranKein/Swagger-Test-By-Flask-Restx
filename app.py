from flask import Flask
from flask_restx import Api
import endpoints

app = Flask(__name__)
app.register_blueprint(endpoints.test1_app)
app.register_blueprint(endpoints.test2_app)

api = Api(app, title='Swagger Test')
api.add_namespace(endpoints.test1_api)
api.add_namespace(endpoints.test2_api)

if __name__ == "__main__":
    app.run()
