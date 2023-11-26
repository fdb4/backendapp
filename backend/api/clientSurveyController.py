from app import api
from flask_restx import Resource, fields
from flask import request, session
from service.clientSurveyService import survey

survey_model=api.model(
    'Survey',
    {
        "clientID":fields.Integer(),
        "height":fields.Float(),
        "weight":fields.Float(),
        "goalweight":fields.Integer(),
        "movement":fields.String(45),
        "age":fields.Integer(),
        "gender":fields.Integer(),
        "cycling":fields.Integer(),
        "strength":fields.Integer(),
        "running":fields.Integer(),
        "sports":fields.Integer(),
        "yoga":fields.Integer(),
        "swimming":fields.Integer(),
        "martialarts":fields.Integer(),
        "other":fields.String(45)
    }
)

@api.route('/survey')
class Survey(Resource):
    @api.expect(survey_model)
    def post(self):
        """Getting info from client surveys"""
        clientID=request.json['clientID']
        height=request.json['height']
        weight=request.json['weight']
        goalweight=request.json['goalweight']
        movement=request.json['movement']
        age=request.json['age']
        gender=request.json['gender']
        cycling=request.json['cycling']
        strength=request.json['strength']
        running=request.json['running']
        sports=request.json['sports']
        yoga=request.json['yoga']
        swimming=request.json['swimming']
        martialarts=request.json['martialarts']
        other=request.json['other']

        resp =  survey(clientID, height, weight, goalweight, movement, age, gender, cycling, strength, running, sports, yoga, swimming, martialarts, other)

        return resp