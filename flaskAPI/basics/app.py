from flask import Flask

"""
Resource allow you to create a resource to connect to using restful api
and Api the wrapper for the app that allow the resource to connect.
"""
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


class Tuna(Resource):

    '''
    Resources class methods:
    1. get
    2. post
    3. put
    4. delete
    '''

    def get(self):
        return {'hello': 'tuna'}


# connect this resource to actual URL.
api.add_resource(Tuna, '/')


if __name__ == '__main__':
    app.run(debug=True)