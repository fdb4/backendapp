from app import api
from flask_restx import Resource, fields
from flask import request,session,jsonify
from service.admincoachService import updateCV

acModel=api.model(
    'acModel',#admin coach Model
    {
        "visible":fields.Boolean
    }
)

@api.route('/admincc/<int:coachexpID>')
class admincc(Resource):
    @api.expect(acModel)
    def put(self, coachexpID):#Note add verification that user is admin
        if session["isadmin"] is None:
            return jsonify({"message":"Error client is not admin"})
        result=updateCV(coachexpID,request.json["visible"])
        return result