from flask_restx import Resource, fields
from flask import Flask, request
from app import api, app
from service.editClientProfileService import edit_client_profile

@api.route('/client/edit/<int:client_id>')
class EditClientProfile(Resource):
    def put(self, client_id):
        data = request.json
        edit_client_profile(
            client_id,
            data.get('firstname'), 
            data.get('lastname'), 
            data.get('email'), 
            data.get('height'), 
            data.get('weight'), 
            data.get('goalweight'), 
            data.get('movement_type'), 
            data.get('age'), 
            data.get('gender')
        )
        return {"message": "Profile updated successfully"}, 200