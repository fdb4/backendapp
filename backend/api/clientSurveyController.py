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
        clientID = request.json.get("clientID")  # Use get() to handle missing key gracefully
        height = request.json.get('height')
        weight = request.json.get('weight')
        goalweight = request.json.get('goalweight')
        movement = request.json.get('movement')
        age = request.json.get('age')
        gender = request.json.get('gender')
        cycling = request.json.get('cycling')
        strength = request.json.get('strength')
        running = request.json.get('running')
        sports = request.json.get('sports')
        yoga = request.json.get('yoga')
        swimming = request.json.get('swimming')
        martialarts = request.json.get('martialarts')
        other = request.json.get('other')

        # Use the retrieved values in your survey function or further processing
        resp = survey(
            clientID, height, weight, goalweight, movement, age, gender,
            cycling, strength, running, sports, yoga, swimming, martialarts, other
        )

        return resp
