# service/get_workout_plan_logs_service.py

from data.exts import db
from sqlalchemy.sql import text
import datetime

def get_workout_plan_logs(client_id):
    query = text("""
        SELECT *
        FROM workoutplanlog
        WHERE clientID = :client_id
    """)
    
    results = db.session.execute(query, {'client_id': client_id}).fetchall()
    
    workout_plan_logs = []
    for row in results:
        row_dict = row._asdict()
        # Convert datetime objects to string
        for key, value in row_dict.items():
            if isinstance(value, datetime.datetime):
                row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        workout_plan_logs.append(row_dict)

    return workout_plan_logs
