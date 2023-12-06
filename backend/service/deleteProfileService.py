from data.models import Clients, CoachExp, Location, State
from data.exts import db
from sqlalchemy.sql import text


def delete_client_profile(client_id):
    fetch_ids_query = text("""
        SELECT geninfoID, workoutgoalID 
        FROM clients 
        WHERE clientID = :client_id
    """)
    ids_result = db.session.execute(fetch_ids_query, {'client_id': client_id}).fetchone()

    if ids_result is None:
        return

    geninfo_id, workoutgoal_id = ids_result

    related_tables = ['clientcoaches', 'dailylog', 'messagetable', 'workoutplan']
    for table in related_tables:
        delete_related_query = text(f"DELETE FROM {table} WHERE clientID = :client_id")
        db.session.execute(delete_related_query, {'client_id': client_id})

    delete_client_query = text("DELETE FROM clients WHERE clientID = :client_id")
    db.session.execute(delete_client_query, {'client_id': client_id})

    if geninfo_id is not None:
        delete_geninfo_query = text("DELETE FROM generalinfo WHERE geninfoID = :geninfo_id")
        db.session.execute(delete_geninfo_query, {'geninfo_id': geninfo_id})

    if workoutgoal_id is not None:
        delete_workoutgoal_query = text("DELETE FROM workoutgoal WHERE workoutgoalID = :workoutgoal_id")
        db.session.execute(delete_workoutgoal_query, {'workoutgoal_id': workoutgoal_id})

    db.session.commit()
