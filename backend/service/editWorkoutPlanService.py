from data.exts import db
from sqlalchemy.sql import text

def update_workouts_in_plan(workoutplanID, workouts):
    try:
        for workout in workouts:
            query = text("""
                UPDATE workoutplan
                SET workoutID = :workoutID, Sets = :Sets, reps = :reps
                WHERE id = :id AND workoutplanID = :workoutplanID
            """)
            db.session.execute(query, {
                'id': workout['id'],
                'workoutID': workout['workoutID'],
                'Sets': workout['Sets'],
                'reps': workout['reps'],
                'workoutplanID': workoutplanID
            })

        db.session.commit()
        return {"message": "Workout plan updated successfully"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
