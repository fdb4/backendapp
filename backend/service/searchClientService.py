from data.exts import db
from sqlalchemy.sql import text

def searchClient(clientID):
        query = text(
                "select c.email, c.firstname, c.lastname "
                "from clients c "
                "where clientID = :cid"
        )
        query = query.bindparams(cid=clientID)
        clients=db.session.execute(query).fetchall()
        return clients