from data.models import Clients, MessageTable
from data.exts import db
from sqlalchemy.orm import aliased
from sqlalchemy.sql import text
from flask import jsonify, session
def getMessage():
    """coach=aliased(Clients)
    Message=db.session.query(

        coach.firstname,
        coach.lastname,
        MessageTable.message,
        MessageTable.Read

    ).join(Clients, MessageTable.clientID == Clients.clientID).join(coach, MessageTable.coachexpID == coach.coachexpID).all()
    Message=Message.filter_by(MessageTable.clientID==session["clientID"])"""
    query = text(

        "select  messagetable.message, coach.firstname, coach.lastname "
        "from messagetable "
        "inner join clients as coach on messagetable.coachexpID=coach.coachexpID"
        " where messagetable.clientID=:CID;")
    query = query.bindparams(CID=session["clientID"])
    Message= db.session.execute(query).fetchall()
    return Message