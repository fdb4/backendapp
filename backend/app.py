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

    @api.marshal_list_with(client_model)
    def post(self):
        """Add a new client"""
        data=request.get_json()
        new_client=Clients(
            client_id=data.get('client_id'),
            email=data.get('email'),
            password=data.get('password'),
            coachID=data.get('coachID'),
            firstname=data.get('firstname'),
            lastname=data.get('lastname')
        )
        new_client.save()
        return new_client,201


@api.route('/clients/<int:client_id>')
class ClientResource(Resource):
    @api.marshal_with(client_model)
    def get(self, client_id):
        """Get a client by id"""
        client=Clients.query.get_or_404(client_id)
        print(client)

        return client

    @api.marshal_with(client_model)
    def put(self, client_id):
        """Update a client by id"""
        client_to_update=Clients.query.get_or_404(client_id)

        data=request.get_json()

        client_to_update.update(data.get('email'), data.get('password'), data.get('firstname'), data.get('lastname'))

        return client_to_update

    @api.marshal_with(client_model)
    def delete(self, client_id):
        """Delete client by Id"""
        client_to_delete=Clients.query.get_or_404(client_id)
        client_to_delete.delete()
        return client_to_delete


@app.shell_context_processor
def make_shell_context():
    return {
        "db": db,
        "Clients": Clients
    }


if __name__ == "__main__":
    app.run()