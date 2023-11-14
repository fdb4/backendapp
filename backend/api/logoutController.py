from app import api
from flask_restx import Resource, fields
from flask import request
from service.logoutService import logoutClient

@api.route('/logout')
class Logout(Resource):
    def get(self):
        """Client logout"""
        return logoutClient("clientID")