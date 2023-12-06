from data.exts import db
from sqlalchemy.sql import text

def getDeactivatedWorkouts():
    query = text(
        "select workoutID, workoutname, videolink, description, musclegroup, equipment "
        "from workoutbank " 
        "where visible = 0; "
    )
    results = db.session.execute(query).fetchall()
    return results