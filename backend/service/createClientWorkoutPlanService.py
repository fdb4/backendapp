# service/create_client_workout_plan_service.py

from data.exts import db
from sqlalchemy.sql import text

def create_client_workout_plan(planName, clientID, workoutID, Sets, reps):
    try:
        # Inserting the new workout plan for the client
        query = text("""
            INSERT INTO workoutplan (planName, clientID, workoutID, Sets, reps, coachexpID)
            VALUES (:planName, :clientID, :workoutID, :Sets, :reps, NULL)
        """)

        db.session.execute(query, {
            'planName': planName,
            'clientID': clientID,
            'workoutID': workoutID,
            'Sets': Sets if Sets is not None else None,
            'reps': reps if reps is not None else None
        })
        db.session.commit()
        return {"message": "Client workout plan created successfully"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
