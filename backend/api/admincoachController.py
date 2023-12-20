from app import api2
from flask_restx import Resource, fields
from flask import request,session,jsonify
from service.admincoachService import updateCV

acModel=api2.model(
    'acModel',#admin coach Model
    {
        "visible":fields.Integer()
    }
)

@api2.route('/admincc/<int:coachexpID>')
class admincc(Resource):
    @api2.expect(acModel)
    def put(self, coachexpID):#Note add verification that user is admin

        result=updateCV(coachexpID,request.json["visible"])
        return result
