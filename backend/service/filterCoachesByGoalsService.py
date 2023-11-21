# filterCoachesByGoalsService.py

from data.models import Clients, CoachExp, Location, State, WorkoutGoal
from data.exts import db
from sqlalchemy.sql import text

def filter_coaches_by_goal(goal):
    sql_query = text(
        """
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
            s.state
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
            wg.:goal = 1
        """
    )
    

    query = sql_query.bindparams(goal=goal)
    results = db.session.execute(query).fetchall()
    return [dict(row) for row in results]
