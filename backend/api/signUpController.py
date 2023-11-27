from app import api
from flask_restx import Resource, fields
from flask import request
from service.signUpService import signUpClient


signup_model=api.model(
    'Signup',
    {
        "email":fields.String(),
        "firstname":fields.String(),
        "lastname":fields.String(),
        "password":fields.String(),
        "userType":fields.Integer()
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
        userType=request.json['userType']
        return signUpClient(email, password, firstname, lastname, userType)
        