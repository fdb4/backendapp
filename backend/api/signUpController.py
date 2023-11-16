from app import api
from flask_restx import Resource, fields
from flask import request
from service.signUpService import signUpClient


signup_model=api.model(
    'Signup',
    {
        "firstname":fields.String(),
        "lastname":fields.String(),
        "email":fields.String(),
        "password":fields.String()
    }
)

@api.route('/signup')
class SignUpResource(Resource):
    @api.expect(signup_model)
    def post(self):
        """Add a new client"""
        email=request.json['email']
        password=request.json['password']
        firstname=request.json['firstname']
        lastname=request.json['lastname']
        return signUpClient(email, password, firstname, lastname)
        