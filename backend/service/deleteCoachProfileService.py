from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text

def delete_coach_profile(client_id):
    coach_check_query = text("""
        SELECT isCoach, coachexpID, workoutgoalID 
        FROM clients 
        WHERE clientID = :client_id
    """)
    coach_check_result = db.session.execute(coach_check_query, {'client_id': client_id}).fetchone()

    if coach_check_result is None or coach_check_result[0] != 1:
        return

    coachexp_id, workoutgoal_id = coach_check_result[1], coach_check_result[2]

    if coachexp_id is not None:
        update_client_query = text("UPDATE clients SET coachexpID = NULL WHERE coachexpID = :coachexp_id")
        db.session.execute(update_client_query, {'coachexp_id': coachexp_id})

    if workoutgoal_id is not None:
        update_client_query = text("UPDATE clients SET workoutgoalID = NULL WHERE workoutgoalID = :workoutgoal_id")
        db.session.execute(update_client_query, {'workoutgoal_id': workoutgoal_id})

    related_tables = ['clientcoaches', 'messagetable', 'workoutplan']
    for table in related_tables:
        delete_related_query = text(f"DELETE FROM {table} WHERE clientID = :client_id")
        db.session.execute(delete_related_query, {'client_id': client_id})

    if coachexp_id is not None:
        delete_coach_query = text("DELETE FROM coachexp WHERE coachexpID = :coachexp_id")
        db.session.execute(delete_coach_query, {'coachexp_id': coachexp_id})

    if workoutgoal_id is not None:
        delete_workoutgoal_query = text("DELETE FROM workoutgoal WHERE workoutgoalID = :workoutgoal_id")
        db.session.execute(delete_workoutgoal_query, {'workoutgoal_id': workoutgoal_id})

    delete_client_query = text("DELETE FROM clients WHERE clientID = :client_id")
    db.session.execute(delete_client_query, {'client_id': client_id})

    db.session.commit()
