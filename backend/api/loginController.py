from app import api
from flask_restx import Resource, fields
from flask import request
from service.loginService import loginClient


login_model=api.model(
    'Login',
    {
        "email":fields.String(),
        "password":fields.String()
    }
)

@api.route('/login')
class LoginResource(Resource):
    @api.expect(login_model)
    def post(self):
        email=request.json['email']
        password=request.json['password']
        return loginClient(email, password)