from data.exts import db
from sqlalchemy.sql import text

def edit_workout_plan(workoutplanID, planName, exercises):
    try:
        # Update planName
        plan_name_query = text("""
            UPDATE workoutplan
            SET planName = :planName
            WHERE workoutplanID = :workoutplanID
        """)
        db.session.execute(plan_name_query, {'planName': planName, 'workoutplanID': workoutplanID})

        # Update exercises
        for exercise in exercises:
            exercise_query = text("""
                UPDATE workoutplan
                SET Sets = :Sets, reps = :reps, workoutID = :workoutID
                WHERE workoutplanID = :workoutplanID
            """)
            db.session.execute(exercise_query, {
                'Sets': exercise['Sets'],
                'reps': exercise['reps'],
                'workoutID': exercise['workoutID'],
                'workoutplanID': workoutplanID
            })

        db.session.commit()
        return {"message": "Workout plan updated successfully"}, 200
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
