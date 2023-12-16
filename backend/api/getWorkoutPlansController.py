
from flask_restx import Api, Resource, fields
from app import api, app
from service.getWorkoutPlansService import get_client_workout_plans

workout_plan_model = api.model(
    "WorkoutPlan",
    {
        "id": fields.Integer(),
        "workoutplanID": fields.Integer(),
        "planName": fields.String(),
        "clientID": fields.Integer(),
        "coachexpID": fields.Integer(),
        "workoutID": fields.Integer(),
        "Sets": fields.Integer(),
        "reps": fields.Integer()
    }
)

@api.route('/workoutplans/client/<int:client_id>')
class ClientWorkoutPlansResource(Resource):
    @api.marshal_list_with(workout_plan_model)
    def get(self, client_id):
        """Retrieve workout plans for a specific client"""
        return get_client_workout_plans(client_id)

if __name__ == '__main__':
    app.run(debug=True)
