# filterCoachesByExperienceService.py
from data.exts import db
from sqlalchemy.sql import text

def filter_coaches_by_experience(min_experience):
    query = text(
    """
    SELECT ce.coachexpID, ce.price, ce.rating, ce.experience, ce.bio, 
           l.gym, l.town, s.state 
    FROM coachexp ce 
    JOIN location l ON ce.locationID = l.locationID 
    JOIN state s ON l.stateID = s.stateID 
    WHERE ce.experience >= :min_experience
    """)

    results = db.session.execute(query, {'min_experience': min_experience}).fetchall()
    return results
