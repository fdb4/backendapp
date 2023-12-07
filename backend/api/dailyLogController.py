from app import api2, app
from flask_restx import Resource, fields
from flask import request
from service.dailyLogService import dailyLog

log_model=api2.model(
    "Daily_Log",
    {
        "clientID":fields.Integer(),
        "calorie":fields.Integer(),
        "water":fields.Integer(),
        "mood":fields.Integer(),
    }

)

@api2.route('/dailyLog')
class DailyLog(Resource):
    @api2.expect(log_model)
    def post(self):
        """Daily Log"""
        clientID=request.json['clientID']
        calorie=request.json['calorie']
        water=request.json['water']
        mood=request.json['mood']
        
        return dailyLog(clientID, calorie, water, mood)