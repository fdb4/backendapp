from data.exts import db
from sqlalchemy.sql import text

def filterWorkoutsByEquipment(equipment):
    similar = f'%{equipment}%'
    query = text(
        "select workoutID, workoutname, videolink, description, musclegroup, equipment "
        "from workoutbank "
        "where equipment like :e and visible = 1;")
    query = query.bindparams(e=similar)

    results = db.session.execute(query).fetchall()
    return results
