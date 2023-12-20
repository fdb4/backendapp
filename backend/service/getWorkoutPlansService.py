
from data.exts import db
from sqlalchemy.sql import text

def get_client_workout_plans(client_id):
    query = text(
    """
    SELECT wp.id, wp.workoutplanID, wp.planName, wp.clientID, wp.coachexpID, 
           wp.workoutID, wp.Sets, wp.reps 
    FROM workoutplan wp
    WHERE wp.clientID = :client_id
    """)

    results = db.session.execute(query, {'client_id': client_id}).fetchall()
    return results
