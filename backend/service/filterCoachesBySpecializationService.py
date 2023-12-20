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
        wg.*
    FROM 
        clients c
    JOIN 
        coachexp ce ON c.coachexpID = ce.coachexpID
    JOIN 
        workoutgoal wg ON c.workoutgoalID = wg.workoutgoalID
    JOIN 
        location l ON ce.locationID = l.locationID
    JOIN 
        state s ON l.stateID = s.stateID
    WHERE 
        (wg.{specialization} = 1 or other is not null) and ce.visible = 0
    """)
    
    results = db.session.execute(query).fetchall()
    coaches = []
    for result in results:
        coach = {
            "clientID": result[0],
            "email": result[1],
            "firstname": result[2],
            "lastname": result[3],
            "price": result[4],
            "rating": result[5],
            "experience": result[6],
            "bio": result[7],
            "gym": result[8],
            "town": result[9],
            "state": result[10],
            "specializations": extract_specializations(result[12:])
        }
        coaches.append(coach)

    return coaches

def extract_specializations(workout_goal_data):
    specializations = []
    specialization_fields = ['cycling', 'strength', 'running', 'sports', 'yoga', 'swimming', 'martialarts', 'other']

    for i, field in enumerate(specialization_fields):
        if workout_goal_data[i] == 1:
            specializations.append(field)

    return specializations
