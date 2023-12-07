from app import api2
from flask_restx import Resource, fields
from flask import request
from service.logoutService import logoutClient

@api2.route('/logout')
class LogoutResource(Resource):
    def get(self):
        """Logout"""
        return logoutClient("clientID")