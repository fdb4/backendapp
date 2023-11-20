from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def filterByStateGym(state, gym):
    query = text(
    "select info2.clientID, info2.email, info2.firstname, info2.lastname, info2.price, info2.rating, info2.experience, info2.bio, info2.gym, info2.town, s.state "
    "from schema.state s "
    "join "
    "(select info.clientID, info.email, info.firstname, info.lastname, info.price, info.rating, info.experience, info.bio, l.gym, l.town, l.stateID "
    "from location l "
    "join( "
    "select c.clientID, c.email, c.firstname, c.lastname, x.price, x.rating, x.experience, x.bio, x.locationID "
    "from schema.clients c "
    "join schema.coachexp x "
    "where c.coachexpid = x.coachexpid) info "
    "where info.locationID = l.locationID and l.gym = :gy) info2 "
    "where info2.stateID = s.StateID and s.state = :st;")
    query = query.bindparams(gy=gym, st=state)

    results = db.session.execute(query).first()
    return results
