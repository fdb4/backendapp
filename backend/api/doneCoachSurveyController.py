from app import api
from flask_restx import Resource, fields
from service.doneCoachSurveyService import doneCoachSurvey

survey_done_model=api.model(
    "Survey_done",
    {
        "survey":fields.Integer()
    }
)

@api.route('/doneCoachSurvey/<int:clientID>')
class doneCoachSurveyResource(Resource):
    @api.marshal_with(survey_done_model)
    def get(self, clientID):
        """Check if coach has signed up survey"""
        return doneCoachSurvey(clientID)