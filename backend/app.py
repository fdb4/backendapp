from flask import Flask, request, jsonify
from flask_restx import Api, Resource, fields
from config import DevConfig
from models import Clients
from exts import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager

app=Flask(__name__)
app.config.from_object(DevConfig)
db.init_app(app)
api=Api(app,doc='/docs')

JWTManager(app) 

client_model=api.model(
    "Clients",
    {
        "client_id":fields.Integer(),
        "email":fields.String(45),
        "password":fields.String(45),
        "coachID":fields.Integer(),
        "firstname":fields.String(45),
        "lastname":fields.String(45)
    }

)

signup_model=api.model(
    'Signup',
    {
        "firstname":fields.String(),
        "lastname":fields.String(),
        "email":fields.String(),
        "password":fields.String()
    }
)


@api.route('/hello')
class HelloResource(Resource):
    def get(self):
        return{"message":"Hello World"}

@api.route('/signup')
class SignUp(Resource):
    @api.expect(signup_model)
    def post(self):
        """Add a new client"""
        data=request.get_json()
        email=data.get('email')
        db_client=Clients.query.filter_by(email=email).first()

        if db_client is not None:
            return jsonify({"message":f"User with email {email} already exists"})

        new_client=Clients(
            email=data.get('email'),
            password=generate_password_hash(data.get('password')),
            firstname=data.get('firstname'),
            lastname=data.get('lastname')
        )
        new_client.save()
        return jsonify({"message": "User created successfuly"})

@api.route('/login')
class Login(Resource):
    def post(self):
        data=request.get_json()

        email=data.get('email')
        password=data.get('password')

        pass

@api.route('/clients')
class ClientsRescource(Resource):

    @api.marshal_list_with(client_model)
    def get(self):
        """Get all Clients"""
        clients=Clients.query.all()
        return clients


@api.route('/clients/<int:client_id>')
class ClientResource(Resource):

    @api.marshal_with(client_model)
    def get(self, client_id):
        """Get a client by id"""
        client=Clients.query.get_or_404(client_id)
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
    return{
        "db":db,
        "Clients":Clients
    }
    

if __name__ == "__main__":
    app.run()