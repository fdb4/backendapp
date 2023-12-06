from data.models import Clients, GeneralInfo
from data.exts import db
from sqlalchemy.sql import text

def getClientProfiles(clientID):
    query = text(
        "select gen.firstname, gen.lastname, gen.email, gen.height, gen.weight, gen.goalweight, gen.movement, gen.age, gen.gender, "
        "w.cycling, w.strength , w.running , w.sports , w.yoga , w.swimming , w.martialarts , w.other "
        "from "
            "(select c.workoutgoalID , c.firstname, c.lastname, c.email, g.height, g.weight, g.goalweight, g.movement, g.age, g.gender "
            "from clients c "
            "join generalinfo g "
            "where c.geninfoID = g.geninfoID and c.clientID = :cid) gen "
        "join workoutgoal w "
        "where gen.workoutgoalID  = w.workoutgoalID "
    )
    query = query.bindparams(cid=clientID)
    results = db.session.execute(query).fetchall()
    return results