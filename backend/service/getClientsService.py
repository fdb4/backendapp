from data.exts import db
from sqlalchemy.sql import text

def getClients():
        query = text(
                "select c.email, c.firstname, c.lastname "
                "from clients c"
        )
        clients=db.session.execute(query).fetchall()
        return clients

