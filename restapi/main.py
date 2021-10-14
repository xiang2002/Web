from flask import Flask
from flask.views import MethodView
from google.cloud import ndb


class Boat(ndb.Model):
    id = ndb.StringProperty()
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty()
    length = ndb.IntegerProperty()
    at_sea = ndb.BooleanProperty()

app = Flask(__name__)

class UserAPI(MethodView):
    
    def get(self, user_id):
        if user_id is None:
            return "user_id None"
        else:
            return "User _id"+str(user_id)

    def post(self):
        # create a new user
        pass

    def delete(self, user_id):
        # delete a single user
        pass

    def put(self, user_id):
        # update a single user
        pass

user_view = UserAPI.as_view('user_api')
app.add_url_rule('/users/', defaults={'user_id': None},
                 view_func=user_view, methods=['GET',])
# app.add_url_rule('/users/', view_func=user_view, methods=['POST',])
# app.add_url_rule('/users/<int:user_id>', view_func=user_view,
#                  methods=['GET', 'PUT', 'DELETE'])
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)