from data.models import Clients, MessageTable
from data.exts import db
from sqlalchemy.sql import text

def getConversations(clientID):
    query = text(
        "select c.clientID, c.firstname, c.lastname "
        "from clients c "
        "join "
            "(select distinct clientID , clientID2 "
            "from messagetable "
            "where clientID = :cid or clientID2 = :cid) info "
        "on c.clientID = info.clientID "
        "where c.clientID != :cid; "
    )

    query = query.bindparams(cid=clientID)
    data=db.session.execute(query).fetchall()
    return data

