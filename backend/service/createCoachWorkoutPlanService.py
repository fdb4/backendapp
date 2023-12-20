from data.exts import db
from sqlalchemy.sql import text

def create_coach_workout_plan(data):
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

        # Get the highest current workoutplanID
        max_id_query = text("SELECT MAX(workoutplanID) FROM workoutplan")
        max_id_result = db.session.execute(max_id_query).scalar()

        # Determine the next workoutplanID
        workoutplanID = 1 if max_id_result is None else max_id_result + 1

        # Insert the workout plan details
        # Assuming each exercise is a separate entry in the 'exercises' list within data
        for exercise in data['exercises']:
            insert_query = text("""
                INSERT INTO workoutplan (planName, clientID, coachexpID, workoutID, Sets, reps, workoutplanID)
                VALUES (:planName, :clientID, :coachexpID, :workoutID, :Sets, :reps, :workoutplanID)
            """)
            db.session.execute(insert_query, {
                'planName': data['planName'],
                'clientID': data['clientID'],
                'coachexpID': coachexpID,
                'workoutID': exercise['workoutID'],
                'Sets': exercise['Sets'],
                'reps': exercise['reps'],
                'workoutplanID': workoutplanID
            })

        db.session.commit()
        return {"message": "Coach workout plan created successfully", "workoutplanID": workoutplanID}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500
