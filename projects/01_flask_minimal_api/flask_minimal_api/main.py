from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


users = {
    # default user list
    '1': 'Joe',
    '2': 'Roger',
    '3': 'Danny',
    '4': 'Brian',
    '5': 'Marc'
}

class User(Resource):
    def get(self, user_id):
        return f"id {user_id} associated with {users[user_id]}"

    def put(self, user_id):
        users[user_id] = request.form['data']
        return f"id {user_id} associated with {users[user_id]}"

class AllUsers(Resource):
    def get(self):
        return users

# endpoint to get and post a user
api.add_resource(User, '/user/<string:user_id>')
# endpoint to get all users
api.add_resource(AllUsers, '/all_users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)