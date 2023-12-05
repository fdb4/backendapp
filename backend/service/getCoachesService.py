from data.exts import db
from sqlalchemy.sql import text

def getCoaches():
    query = text(
        """
        SELECT 
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
                    schema.coachexp x ON c.coachexpid = x.coachexpid) info ON info.locationID = l.locationID) info2 ON info2.stateID = s.StateID 
        JOIN 
            schema.workoutgoal wg ON info2.workoutgoalID = wg.workoutgoalID;
        """
    )

    results = db.session.execute(query).fetchall()

    coaches = []
    for result in results:
        coach = {
            "email": result[0],
            "firstname": result[1],
            "lastname": result[2],
            "price": result[3],
            "rating": result[4],
            "experience": result[5],
            "bio": result[6],
            "gym": result[7],
            "town": result[8],
            "state": result[9],
            "specializations": extract_specializations(result[10:])
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
