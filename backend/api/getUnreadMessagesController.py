from flask_restx import Resource, fields
from flask import Flask, request
from app import api, app
from service.getUnreadMessagesService import get_unread_message_count

@api.route('/notifications/count/<int:user_id>')
class NotificationCountResource(Resource):
    def get(self, user_id):
        """Get count of unread messages for a user"""
        unread_count = get_unread_message_count(user_id)
        return {'unread_message_count': unread_count}
