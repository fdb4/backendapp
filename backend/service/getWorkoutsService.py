from data.exts import db
from sqlalchemy.sql import text

def getWorkouts():
    query = text(
        "select workoutID, workoutname, videolink, description, musclegroup, equipment "
        "from workoutbank; "
    )
    results = db.session.execute(query).fetchall()
    return results
