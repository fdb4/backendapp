from data.models import MessageTable
from data.exts import db
from sqlalchemy.orm import aliased
from sqlalchemy.sql import text
from sqlalchemy import update;
from flask import jsonify, session
from service.getMessageService import getMessage
def postMessage(clientIDS,clientIDR,messageT):#paramter clientID is who it is being sent to

    #NOTE: message table has two clientIDs the first clientID is the client logged in
    #The Second is the other recipient
    new_message=MessageTable(
        clientID=clientIDS,
        clientID2=clientIDR,
        message=messageT,
        MSender=clientIDS,
        MReciever =clientIDR,
        MRead=True
    )
    new_message.save()
    # Two instances are created in order to manage the read column
    # Wouldn't make sense for the entry to be considered read for both partys if the other never saw it
    new_message2=MessageTable(
        clientID=clientIDR,
        clientID2=clientIDS,
        message=messageT,
        MSender=clientIDS,
        MReciever =clientIDR
    )
    new_message2.save()
    return jsonify({"message": "Message successfuly sent"})
