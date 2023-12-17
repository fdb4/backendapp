from data.exts import db
from sqlalchemy.sql import text

def edit_workout_plan(clientID, workoutplanID, data):
    try:
        # Delete existing workouts with the given workoutplanID for the client
        delete_query = text("""
            DELETE FROM workoutplan 
            WHERE clientID = :clientID AND workoutplanID = :workoutplanID
        """)
        db.session.execute(delete_query, {'clientID': clientID, 'workoutplanID': workoutplanID})

        # Insert new workouts
        for exercise in data['exercises']:
            insert_query = text("""
                INSERT INTO workoutplan (planName, clientID, workoutplanID, workoutID, Sets, reps)
                VALUES (:planName, :clientID, :workoutplanID, :workoutID, :Sets, :reps)
            """)
            db.session.execute(insert_query, {
                'planName': data['planName'],
                'clientID': clientID,
                'workoutplanID': workoutplanID,
                'workoutID': exercise['workoutID'],
                'Sets': exercise['Sets'],
                'reps': exercise['reps']
            })

        db.session.commit()
        return {"message": "Workout plan updated successfully"}, 200

    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
