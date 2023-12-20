from data.exts import db
from sqlalchemy.sql import text

def filterWorkoutsByMuscleGroup(musclegroup):
    similar = f'%{musclegroup}%'
    query = text(
        "select workoutID, workoutname, videolink, description, musclegroup, equipment "
        "from workoutbank "
        "where musclegroup like :n and visible = 1;")
    query = query.bindparams(n=similar)

    results = db.session.execute(query).fetchall()
    return results
