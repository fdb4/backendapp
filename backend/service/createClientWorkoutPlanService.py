from data.exts import db
from sqlalchemy.sql import text

def create_client_workout_plan(data):
    try:
        # Inserting the new workout plan for the client
        insert_query = text("""
            INSERT INTO workoutplan (planName, clientID, workoutID, Sets, reps, coachexpID)
            VALUES (:planName, :clientID, :workoutID, :Sets, :reps, NULL)
        """)
        db.session.execute(insert_query, {
            'planName': data['planName'],
            'clientID': data['clientID'],
            'workoutID': data['workoutID'],
            'Sets': data['Sets'] if 'Sets' in data else None,
            'reps': data['reps'] if 'reps' in data else None
        })
        db.session.commit()
        return {"message": "Client workout plan created successfully"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
