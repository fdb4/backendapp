from sqlalchemy.sql import text
from data.exts import db
from . import searchCoachService
from data.models import Clients

def getCurrentCoach(clientID):
    print(clientID)
    query = text (
        "select coachexpID from clientcoaches where clientID = :cid and request = 1"
    )
    
    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).first()
    print(results)
    if results is None:
        return {"message": "No Coach available"}
    coachexpID = results.coachexpID
    coach = Clients.query.filter_by(coachexpID=coachexpID).first()
    return searchCoachService.searchCoach(coach.clientID)