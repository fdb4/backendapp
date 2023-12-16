from flask_restx import Api, Resource, fields
from app import api, app
from service.getWorkoutPlanLogService import get_client_workout_logs

workout_log_model = api.model(
    "WorkoutLog",
    {
        "planName": fields.String(),
        "workoutplanID": fields.Integer(),
        "clientID": fields.Integer(),
        "workoutID": fields.Integer(),
        "sets": fields.Integer(),
        "reps": fields.Integer(),
        "lastmodified": fields.DateTime()
    }
)

@api.route('/workoutlogs/client/<int:client_id>')
class ClientWorkoutLogsResource(Resource):
    @api.marshal_list_with(workout_log_model)
    def get(self, client_id):
        """Retrieve workout log progress for a specific client"""
        return get_client_workout_logs(client_id)

if __name__ == '__main__':
    app.run(debug=True)
