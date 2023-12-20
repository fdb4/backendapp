from app import api2
from flask_restx import Resource, fields
from flask import request
from service.loginService import loginClient


login_model=api2.model(
    'Login',
    {
        "email":fields.String(),
        "password":fields.String()
    }
)

@api2.route('/login')
class LoginResource(Resource):
    @api2.expect(login_model)
    def post(self):
        email=request.json['email']
        password=request.json['password']
        return loginClient(email, password)