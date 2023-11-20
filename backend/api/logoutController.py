from app import api
from flask_restx import Resource, fields
from flask import request
from service.logoutService import logoutClient
from flask_jwt_extended import jwt_required

@api.route('/logout')
class LogoutResource(Resource):
    @jwt_required()
    def get(self):
        """Logout"""
        return logoutClient("clientID")