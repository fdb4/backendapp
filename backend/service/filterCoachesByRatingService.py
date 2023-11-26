# filterCoachesByRatingService.py
from data.exts import db
from sqlalchemy.sql import text

def filter_coaches_by_rating(sort_order='desc'):
    if sort_order not in ['asc', 'desc']:
        sort_order = 'desc'  # Default to descending if invalid sort_order is provided

    query = text(
    """
    SELECT ce.coachexpID, ce.price, ce.rating, ce.experience, ce.bio, 
           l.gym, l.town, s.state 
    FROM coachexp ce 
    JOIN location l ON ce.locationID = l.locationID 
    JOIN state s ON l.stateID = s.stateID 
    ORDER BY ce.rating {}
    """.format(sort_order))

    results = db.session.execute(query).fetchall()
    return results
