from data.exts import db
from sqlalchemy.sql import text

def editWorkout(workout_id, workoutname, videolink, description, musclegroup, equipment):
    query = text("""
    UPDATE workoutbank
    SET 
        workoutname = :workoutname, 
        videolink = :videolink, 
        description = :description, 
        musclegroup = :musclegroup, 
        equipment = :equipment
    WHERE 
        workoutID = :workout_id
    """)

    db.session.execute(query, {
        'workout_id': workout_id,
        'workoutname': workoutname,
        'videolink': videolink,
        'description': description,
        'musclegroup': musclegroup,
        'equipment': equipment
    })
    db.session.commit()
