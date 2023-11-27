from app import api, app
from flask_restx import Resource, fields
from service.getMessageService import getMessage

message_model=api.model(
    "message",
    {
        "message":fields.String,
        "firstname":fields.String(45),#NOTE:this only has coach firstname and lastname
        "lastname":fields.String(45),
        "Read":fields.Boolean(), #NOTE 0 by default
    }

)

@api.route('/message')
class GenMessageRescource(Resource):
    @api.marshal_list_with(message_model)
    def get(self):
        """Get all messages"""
        info = getMessage()
        return info