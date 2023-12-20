
from flask_restx import api, Resource, fields
from app import api2, app
from service.getWorkoutPlansService import get_client_workout_plans

workout_plan_model = api2.model(
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

@api2.route('/workoutplans/client/<int:client_id>')
class ClientWorkoutPlansResource(Resource):
    @api2.marshal_list_with(workout_plan_model)
    def get(self, client_id):
        """Retrieve workout plans for a specific client"""
        return get_client_workout_plans(client_id)

if __name__ == '__main__':
    app.run(debug=True)
