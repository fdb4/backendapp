from app import api, app
from flask_restx import Resource, fields
from service.getClientWorkoutGoalService import getClientWorkoutGoal
from flask_jwt_extended import jwt_required

workoutGoalClient_model=api.model(
    "workoutGoalClient",
    {
        "firstname":fields.String(45),
        "lastname":fields.String(45),
        "email":fields.String(45),
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

@api.route('/workoutGoalInfo/<int:clientID>')
class ClientsWorkoutRescource(Resource):
    @api.marshal_list_with(workoutGoalClient_model)
    @jwt_required()
    def get(self, clientID):
        """Get Workout Goal Information by ClientID"""
        info = getClientWorkoutGoal(clientID)
        
        return info