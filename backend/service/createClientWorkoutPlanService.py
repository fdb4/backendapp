from data.exts import db
from sqlalchemy.sql import text

def create_workout_plan(data):
    try:
        max_id_query = text("SELECT MAX(workoutplanID) FROM workoutplan")
        result = db.session.execute(max_id_query).scalar()

        workoutplanID = 1 if result is None else result + 1


        for exercise in data['exercises']:
            insert_query = text("""
                INSERT INTO workoutplan (planName, clientID, workoutID, Sets, reps, workoutplanID)
                VALUES (:planName, :clientID, :workoutID, :Sets, :reps, :workoutplanID)
            """)
            db.session.execute(insert_query, {
                'planName': data['planName'],
                'clientID': data['clientID'],
                'workoutID': exercise['workoutID'],
                'Sets': exercise['Sets'],
                'reps': exercise['reps'],
                'workoutplanID': workoutplanID
            })

        db.session.commit()
        return {"message": "Workout plan created successfully", "workoutplanID": workoutplanID}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
