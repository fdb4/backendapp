from flask import jsonify
from sqlalchemy.sql import text
from data.exts import db

def unsendRequest(clientID, coachID):
    query = text(
            "select c.coachexpID "
            "from clients c "
            "where clientID = :cid"
    )
    query = query.bindparams(cid=coachID)
    coach=db.session.execute(query).first()

    coachexpID = coach.coachexpID
    if coachexpID == None:
        return {"message": "User is not a coach"}

    query = text(
        """
        delete from clientcoaches where clientID=:cid and coachexpid = :ceid
        """
    )
    query = query.bindparams(cid=clientID, ceid=coachexpID)
    db.session.execute(query)
    db.session.commit()
    return jsonify({"message": "Request unsent successfully"})
