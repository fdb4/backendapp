from sqlalchemy.sql import text
from data.exts import db
from . import searchCoachService

def getActiveRequest(clientID):
    query = text (
        "select coachexpID from clientcoaches where clientID = :cid and request IS NULL"
    )

    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).first()
    if results is None:
        return {"message": "No pending requests"}
    coachexpID = results.coachexpID
    return searchCoachService.searchCoach(coachexpID)