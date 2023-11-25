from app import api
from flask_restx import Resource, fields
from service.doneSurveyService import doneSurvey

survey_done_model=api.model(
    "Survey_done",
    {
        "survey":fields.Integer()
    }
)

@api.route('/doneSurvey/<int:clientID>')
class doneSurveyResource(Resource):
    @api.marshal_with(survey_done_model)
    def get(self, clientID):
        """Check if client has done survey"""
        return doneSurvey(clientID)