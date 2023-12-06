from app import api, app
from flask_restx import Resource, fields
from flask import request
from service.workoutVisibilityService import workoutVisibility

visible_model=api.model(
    "Visible_Model",
    {
        "workoutID":fields.Integer(),
        "visible":fields.Integer()

    }

)
@api.route('/workouts/visibility')
class workoutVisibilityResource(Resource):
    @api.expect(visible_model)
    def post(self):
        """Activate or deactivate a workout: 1 = visible, 0 = invisible"""
        workoutID=request.json['workoutID']
        visible=request.json['visible']
        return workoutVisibility(workoutID, visible)