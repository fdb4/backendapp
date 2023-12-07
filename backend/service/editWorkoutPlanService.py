
from data.exts import db
from sqlalchemy.sql import text

def edit_workout_plan(workoutplanID, data):
    try:
        query = text("""
            UPDATE workoutplan
            SET planName = :planName, Sets = :Sets, reps = :reps
            WHERE workoutplanID = :workoutplanID
        """)
        db.session.execute(query, {
            'planName': data['planName'],
            'Sets': data['Sets'],
            'reps': data['reps'],
            'workoutplanID': workoutplanID
        })
        db.session.commit()
        return {"message": "Workout plan updated successfully"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
