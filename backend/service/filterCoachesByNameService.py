# filterCoachesByNameService.py
from data.exts import db
from sqlalchemy.sql import text

def filter_coaches_by_full_name(first_name, last_name):
    query = text(
    """
    SELECT c.clientID, c.email, c.firstname, c.lastname, ce.price, ce.rating, 
           ce.experience, ce.bio, l.gym, l.town, s.state 
    FROM clients c 
    JOIN coachexp ce ON c.coachexpID = ce.coachexpID 
    JOIN location l ON ce.locationID = l.locationID 
    JOIN state s ON l.stateID = s.stateID 
    WHERE c.firstname LIKE :first_name AND c.lastname LIKE :last_name
    """)

    first_name_like = f"%{first_name}%"
    last_name_like = f"%{last_name}%"
    results = db.session.execute(query, {'first_name': first_name_like, 'last_name': last_name_like}).fetchall()
    return results
