from data.models import Clients, MessageTable
from data.exts import db
from sqlalchemy.orm import aliased
from sqlalchemy.sql import text
from sqlalchemy import update;
from flask import jsonify, session
def getMessage(clientID1,clientID):
    """coach=aliased(Clients)
    Message=db.session.query(

        coach.firstname,
        coach.lastname,
        MessageTable.message,
        MessageTable.Read

    ).join(Clients, MessageTable.clientID == Clients.clientID).join(coach, MessageTable.coachexpID == coach.coachexpID).all()
    Message=Message.filter_by(MessageTable.clientID==session["clientID"])"""#have this cause why not
    query = text(
        "SELECT  messagetable.message, sender.clientID as SenderID, sender.firstname as SenderFN,sender.lastname as SenderLN ,Reciever.firstname,Reciever.lastname,messagetable.lastmodified "
        "FROM messagetable "
        " inner join clients as Sender on messagetable.MSender=sender.clientID"
        " inner join clients as Reciever on messagetable.MReciever=Reciever.clientID"
        " where messagetable.clientID=:SID and messagetable.clientID2=:RID;")
    query = query.bindparams(SID=clientID1,RID=clientID)
    Message= db.session.execute(query).fetchall()
    return Message
