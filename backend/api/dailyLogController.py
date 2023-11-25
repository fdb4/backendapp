from app import api, app
from flask_restx import Resource, fields
from flask import request
from service.dailyLogService import dailyLog

log_model=api.model(
    "Daily_Log",
    {
        "clientID":fields.Integer(),
        "calorie":fields.Integer(),
        "water":fields.Integer(),
        "mood":fields.Integer(),
    }

)

@api.route('/dailyLog')
class DailyLog(Resource):
    @api.expect(log_model)
    def post(self):
        """Daily Log"""
        clientID=request.json['clientID']
        calorie=request.json['calorie']
        water=request.json['water']
        mood=request.json['mood']
        
        return dailyLog(clientID, calorie, water, mood)