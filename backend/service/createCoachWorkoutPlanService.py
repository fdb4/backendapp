from data.exts import db
from sqlalchemy.sql import text

def create_workout_plan(data):
    try:
        # Fetch coachexpID associated with the client
        coach_client_query = text("""
            SELECT cc.coachexpID 
            FROM clientcoaches cc
            JOIN clients c ON cc.clientID = c.clientID
            WHERE cc.clientID = :clientID
        """)
        result = db.session.execute(coach_client_query, {'clientID': data['clientID']}).fetchone()
        coachexpID = result[0] if result else None

        if coachexpID is None:
            return {"error": "Coach experience ID not found for the given client."}, 400

        # Insert the new workout plan
        insert_query = text("""
            INSERT INTO workoutplan (planName, clientID, coachexpID, workoutID, Sets, reps)
            VALUES (:planName, :clientID, :coachexpID, :workoutID, :Sets, :reps)
        """)
        db.session.execute(insert_query, {
            'planName': data['planName'],
            'clientID': data['clientID'],
            'coachexpID': coachexpID,
            'workoutID': data['workoutID'],
            'Sets': data['Sets'] if 'Sets' in data else None,
            'reps': data['reps'] if 'reps' in data else None
        })
        db.session.commit()
        return {"message": "Workout plan created successfully"}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
