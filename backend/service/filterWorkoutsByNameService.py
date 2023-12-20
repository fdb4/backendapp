from data.exts import db
from sqlalchemy.sql import text

def filterWorkoutsByName(name):
    similar = f'%{name}%'
    query = text(
        "select workoutID, workoutname, videolink, description, musclegroup, equipment "
        "from workoutbank "
        "where workoutname like :n and visible = 1;")
    query = query.bindparams(n=similar)

    results = db.session.execute(query).fetchall()
    return results
