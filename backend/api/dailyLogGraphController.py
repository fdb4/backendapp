from app import api2, app
from flask_restx import Resource, fields
from flask import request
from service.dailyLogGraphService import dailyLogGraph

log_graph_model=api2.model(
    "Log_Graph",
    {
        "date":fields.Date(),
        "calorie":fields.Integer(),
        "water":fields.Integer(),
        "mood":fields.Integer(),
    }

)

@api2.route('/dailyLog-data/<int:clientID>')
class dailyLogGraphResource(Resource):
    @api2.marshal_list_with(log_graph_model)
    def get(self, clientID):
        """Daily Log Graph Points"""
        
        return dailyLogGraph(clientID)