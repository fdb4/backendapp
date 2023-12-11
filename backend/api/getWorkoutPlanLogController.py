# api/get_workout_plan_logs_controller.py

from flask_restx import Resource
from app import api
from service.getWorkoutPlanLogService import get_workout_plan_logs

@api.route('/get/workoutplanlog/<int:client_id>')
class WorkoutPlanLogsResource(Resource):
    def get(self, client_id):
        """Fetch workout plan logs for a specific client"""
        return get_workout_plan_logs(client_id)
