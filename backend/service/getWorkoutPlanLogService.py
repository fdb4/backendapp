from data.exts import db
from sqlalchemy.sql import text

def get_client_workout_logs(client_id):
    query = text(
    """
    SELECT wpl.planlogID, wpl.clientID, wpl.workoutID, wpl.sets, wpl.reps, 
           wpl.workoutplanID, wpl.lastmodified
    FROM workoutplanlog wpl
    WHERE wpl.clientID = :client_id
    """)

    results = db.session.execute(query, {'client_id': client_id}).fetchall()
    return results
