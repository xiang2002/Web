from flask import Flask,request
from flask.views import MethodView
from google.cloud import ndb
import json


class Boat(ndb.Model):
    id = ndb.StringProperty()
    name = ndb.StringProperty(required=True)
    type = ndb.StringProperty()
    length = ndb.IntegerProperty()
app = Flask(__name__)
class BoatAPI(MethodView):
    def get(self, boat_id):
        if boat_id is None:
            return "boat_id None"
        else:
            return "boat_id"+str(boat_id)
    def post(self):
        boat_data = json.loads(request.get_data(as_text=True))
        new_boat = Boat(name=boat_data['name'])
        if boat_data.get('type'):
            new_boat.type = boat_data['type']
        if boat_data.get('length'):
            new_boat.length = boat_data['length']
        new_boat.put()
        new_boat.id = new_boat.key.urlsafe()
        new_boat.put()
        boat_dict = new_boat.to_dict()
        boat_dict['self'] = '/boat/' + new_boat.id
        return json.dumps(boat_dict)

    def delete(self, boat_id):
        # delete a single user
        pass

    def put(self, boat_id):
        # update a single user
        pass

boat_view = BoatAPI.as_view('boat_api')
app.add_url_rule('/boats/', defaults={'boat_id': None},
                 view_func=boat_view, methods=['GET',])
app.add_url_rule('/boats/', view_func=boat_view, methods=['POST',])
app.add_url_rule('/boats/<int:boat_id>', view_func=boat_view,
                 methods=['GET', 'PUT', 'DELETE'])
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)