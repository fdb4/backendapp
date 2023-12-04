from app import api
from flask_restx import Resource, fields
from service.deleteCoachProfileService import delete_coach_profile

@api.route('/coach/delete/<int:coach_id>')
class DeleteCoachProfileResource(Resource):
    def delete(self, coach_id):
        """Delete a coach's profile"""
        delete_coach_profile(coach_id)
        return {"message": "Coach profile deleted successfully"}, 200
