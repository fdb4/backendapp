from data.exts import db
from sqlalchemy.sql import text

def get_client_workout_logs(client_id):
    query = text(
    """
    SELECT DISTINCT wpl.planlogID, wpl.clientID, wpl.workoutID, wpl.sets, wpl.reps, 
           wpl.workoutplanID, wp.planName, wpl.lastmodified
    FROM workoutplanlog wpl
    JOIN workoutplan wp ON wpl.workoutplanID = wp.workoutplanID
    WHERE wpl.clientID = :client_id
    ORDER BY wpl.planlogID
    """)

    results = db.session.execute(query, {'client_id': client_id}).fetchall()
    return results
