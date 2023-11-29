from sqlalchemy.sql import text
from data.exts import db

def dailyLogGraph(clientID):
    query = text(
        "select date, calorie, water, mood "
        "from dailylog "
        "where clientID = :cid "
    )
    query = query.bindparams(cid=clientID)
    data=db.session.execute(query).fetchall()
    return data
