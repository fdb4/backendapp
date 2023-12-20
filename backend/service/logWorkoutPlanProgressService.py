from data.exts import db
from sqlalchemy.sql import text

def log_workout_progress(data):
    try:
        for exercise in data['exerciseLogs']:
            insert_query = text("""
                INSERT INTO workoutplanlog (clientID, workoutID, sets, reps, workoutplanID)
                VALUES (:clientID, :workoutID, :sets, :reps, :workoutplanID)
            """)
            db.session.execute(insert_query, {
                'clientID': data['clientID'],
                'workoutID': exercise['workoutID'],
                'sets': exercise['sets'],
                'reps': exercise['reps'],
                'workoutplanID': data['workoutplanID']
            })
        db.session.commit()
        return {"message": "Workout progress logged successfully"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
