from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def filterByGym(gym):
    similar = f'%{gym}%'
    query = text(
        """
        SELECT 
            info2.clientID,
            info2.email, 
            info2.firstname, 
            info2.lastname, 
            info2.price, 
            info2.rating, 
            info2.experience, 
            info2.bio, 
            info2.gym, 
            info2.town, 
            s.state,
            wg.*
        FROM 
            schema.state s 
        JOIN 
            (SELECT 
                info.clientID,
                info.email, 
                info.firstname, 
                info.lastname, 
                info.price, 
                info.rating, 
                info.experience, 
                info.bio, 
                l.gym, 
                l.town, 
                l.stateID, 
                info.workoutgoalID
             FROM 
                location l 
             JOIN 
                (SELECT 
                    c.clientID, 
                    c.email, 
                    c.firstname, 
                    c.lastname, 
                    x.price, 
                    x.rating, 
                    x.experience, 
                    x.bio, 
                    x.locationID, 
                    c.workoutgoalID
                 FROM 
                    schema.clients c 
                 JOIN 
                    schema.coachexp x ON c.coachexpid = x.coachexpid where x.visible=0) info ON info.locationID = l.locationID where l.gym like :gy) info2 ON info2.stateID = s.StateID 
        JOIN 
            schema.workoutgoal wg ON info2.workoutgoalID = wg.workoutgoalID;
        """
    )
    query = query.bindparams(gy=similar)

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
