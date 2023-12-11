from sqlalchemy.sql import text
from data.exts import db
from . import searchCoachService

def getCurrentCoach(clientID):
    query = text (
        "select coachexpID from clientcoaches where clientID = :cid"
    )

    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).first()
    coachexpID = results.coachexpID
    return searchCoachService.searchCoach(coachexpID)