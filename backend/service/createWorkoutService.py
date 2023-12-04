from data.exts import db
from sqlalchemy.sql import text

def createWorkout(workoutname, videolink, description, musclegroup, equipment):
    query = text("""
    INSERT INTO workoutbank (workoutname, videolink, description, musclegroup, equipment)
    VALUES (:workoutname, :videolink, :description, :musclegroup, :equipment)
    """)

    db.session.execute(query, {
        'workoutname': workoutname,
        'videolink': videolink,
        'description': description,
        'musclegroup': musclegroup,
        'equipment': equipment
    })
    db.session.commit()
