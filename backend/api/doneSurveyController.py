from app import api2
from flask_restx import Resource, fields
from service.doneSurveyService import doneSurvey

survey_done_model=api2.model(
    "Survey_done",
    {
        "survey":fields.Integer()
    }
)

@api2.route('/doneSurvey/<int:clientID>')
class doneSurveyResource(Resource):
    @api2.marshal_with(survey_done_model)
    def get(self, clientID):
        """Check if client has done survey"""
        return doneSurvey(clientID)