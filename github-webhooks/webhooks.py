from flask import Flask
from flask_restful import Resource, Api
import os

buildBranch = 'master'
buildPath = '/home/rbf070962/lab-socket-programing/'
buildCommend = 'cd ' + buildPath + ' && git stash && git pull origin ' + buildBranch

app = Flask(__name__)
api = Api(app)

class SetDeploy(Resource):
    def post(self):
        os.system(buildCommend)
        return {'status': 'success'}

api.add_resource(SetDeploy, '/deploy')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
