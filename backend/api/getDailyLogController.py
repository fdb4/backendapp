from flask_restx import Resource
from app import api2
from service.getDailyLogService import get_daily_logs

@api2.route('/get/dailylog/<int:client_id>')
class GetDailyLogResource(Resource):
    def get(self, client_id):
        """Get daily logs for a client"""
        return get_daily_logs(client_id)
