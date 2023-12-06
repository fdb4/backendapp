from data.exts import db
from sqlalchemy.sql import text

def viewCoachClients(clientID):
        query = text(
                "select c.coachexpID "
                "from clients c "
                "where clientID = :cid"
        )
        query = query.bindparams(cid=clientID)
        coach=db.session.execute(query).first()

        coachexpID = coach.coachexpID
        if coachexpID == None:
            return {"message": "User is not a coach"}
        query = text(
                "select c.clientID, c.firstname, c.lastname "
                "from clients c "
                "join( "
                "select * "
                "from clientcoaches c "
                "where coachexpID = :cid and request = 1) info "
                "where info.clientID = c.clientID "
        )

        query = query.bindparams(cid=coachexpID)
        requests=db.session.execute(query).fetchall()

        return requests