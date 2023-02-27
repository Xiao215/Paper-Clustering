from flask import Flask
from flask_restful import Resource, Api
from api.cohere_api import cluster
app = Flask(__name__)
api = Api(app)


class CohereAPi(Resource):
    def get(self):
        return cluster()


api.add_resource(CohereAPi, '/')

if __name__ == '__main__':
    app.run(debug=True)
