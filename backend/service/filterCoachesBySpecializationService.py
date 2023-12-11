from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def filterBySpecialization(specialization):
    # Ensure specialization is a valid column name to avoid SQL injection
    valid_specializations = ['cycling', 'strength', 'running', 'sports', 'yoga', 'swimming', 'martialarts', 'other']
    if specialization not in valid_specializations:
        raise ValueError("Invalid specialization")

    query = text(f"""
    SELECT 
        c.clientID, 
        c.email, 
        c.firstname, 
        c.lastname, 
        ce.price, 
        ce.rating, 
        ce.experience, 
        ce.bio, 
        l.gym, 
        l.town, 
        s.state,
        '{specialization}' AS specialization
    FROM 
        clients c
    JOIN 
        coachexp ce ON c.coachexpID = ce.coachexpID where ce.visible = 0
    JOIN 
        workoutgoal wg ON c.workoutgoalID = wg.workoutgoalID
    JOIN 
        location l ON ce.locationID = l.locationID
    JOIN 
        state s ON l.stateID = s.stateID
    WHERE 
        wg.{specialization} = 1
    """)
    
    results = db.session.execute(query).fetchall()
    return results
