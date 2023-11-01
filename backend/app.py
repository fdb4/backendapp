from flask import Flask, request
from flask_restx import Api, Resource, fields
# from flask_cors import CORS
from config.models import Clients
from config.exts import db
from config.dbcon import dbcon
app = Flask(__name__)
dbc=dbcon.ctdb()
# CORS(app)
db.init_app(app)
api = Api(app, doc='/docs')

# model (serializer)
client_model = api.model(
    "Clients",
    {
        "client_id": fields.Integer(),
        "email": fields.String(45),
        "password": fields.String(45),
        "coachID": fields.Integer(),
        "firstname": fields.String(45),
        "lastname": fields.String(45)
    }

)


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return {"message": "Hello World"}


@api.route('/clients')
class ClientsRescource(Resource):

    @api.marshal_list_with(client_model)
    def get(self):
        """Get all Clients"""
        clients = Clients.query.all()
        return clients

    def post(self):
        """Add a new client"""
        pass


@api.route('/clients/<int:client_id>')
class ClientResource(Resource):
    def get(self, id):
        """Get a client by id"""
        pass

    def put(self, id):
        """Update a client by id"""
        pass

    def delete(self, id):
        """Delete client by Id"""


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Clients": Clients
    }


if __name__ == "__main__":
    app.run()