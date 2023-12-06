from data.models import Clients
from sqlalchemy.sql import text
from data.exts import db



def handleRequest(coachID, clientID, decision):
    coach = Clients.query.filter_by(clientID=coachID).first()
    coachexpID = coach.coachexpID
    if coachexpID is None:
        return {"message":"User is not a coach"},401
    
    query = text(
        "update clientcoaches "
        "set request = :dec "
        "where clientID = :cid and coachexpID = :ceid; "
    )
    query = query.bindparams(dec=decision,cid=clientID,ceid=coachexpID)
    db.session.execute(query)
    db.session.commit()

    return {"message": "Update successful"}



    

        
    