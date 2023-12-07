from app import api2
from flask_restx import Resource, fields
from service.doneCoachSurveyService import doneCoachSurvey

survey_done_model=api2.model(
    "Survey_done",
    {
        "survey":fields.Integer()
    }
)

@api2.route('/doneCoachSurvey/<int:clientID>')
class doneCoachSurveyResource(Resource):
    @api2.marshal_with(survey_done_model)
    def get(self, clientID):
        """Check if coach has signed up survey"""
        return doneCoachSurvey(clientID)