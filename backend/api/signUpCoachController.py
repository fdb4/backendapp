from app import api
from flask_restx import Resource, fields
from flask import request, session
from service.signUpCoachService import signUpCoach

coach_signup_model=api.model(
    'Coach_SignUp',
    {
        "clientID":fields.Integer(),
        "price":fields.Float(),
        "experience":fields.Date(),
        "bio":fields.String(4294967295),
        "gym":fields.String(45),
        "town":fields.String(45),
        "state":fields.String(45)
    }
)

@api.route('/coachSignUp')
class CoachSignUpResource(Resource):
    @api.expect(coach_signup_model)
    def post(self):
        """Getting info from new coaches"""
        coachID = request.json['clientID']
        price = request.json['price']
        experience = request.json['experience']
        bio = request.json['bio']
        gym = request.json['gym']
        town = request.json['town']
        state = request.json['state']

        resp = signUpCoach(coachID, price, experience, bio, gym, town, state)
        return resp
