from app import api
from flask_restx import Resource, fields
from service.deleteProfileService import delete_client_profile

@api.route('/client/delete/<int:client_id>')
class DeleteClientProfileResource(Resource):
    def delete(self, client_id):
        """Delete a client's profile"""
        delete_client_profile(client_id)
        return {"message": "Client profile deleted successfully"}, 200



