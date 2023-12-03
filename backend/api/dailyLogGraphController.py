from app import api, app
from flask_restx import Resource, fields
from flask import request
from service.dailyLogGraphService import dailyLogGraph

log_graph_model=api.model(
    "Log_Graph",
    {
        "date":fields.Date(),
        "calorie":fields.Integer(),
        "water":fields.Integer(),
        "mood":fields.Integer(),
    }

)

@api.route('/dailyLog-data/<int:clientID>')
class dailyLogGraphResource(Resource):
    @api.marshal_list_with(log_graph_model)
    def get(self, clientID):
        """Daily Log Graph Points"""
        
        return dailyLogGraph(clientID)