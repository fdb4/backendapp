from sqlalchemy.sql import text
from data.exts import db
from . import searchCoachService

def getCurrentCoach(clientID):
    query = text (
        "select coachexpID from clientcoaches where clientID = :cid and request = 1"
    )
    
    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).first()
    if results is None:
        return {"message": "No Coach available"}
    coachexpID = results.coachexpID
    return searchCoachService.searchCoach(coachexpID)