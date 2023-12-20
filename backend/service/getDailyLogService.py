from data.exts import db
from sqlalchemy.sql import text
import datetime

def get_daily_logs(client_id):
    query = text("""
        SELECT *
        FROM dailylog
        WHERE clientID = :client_id
    """)

    results = db.session.execute(query, {'client_id': client_id}).fetchall()

    daily_logs = []
    for row in results:
        row_dict = row._asdict()
        # Convert datetime and date objects to string
        for key, value in row_dict.items():
            if isinstance(value, (datetime.datetime, datetime.date)):
                row_dict[key] = value.strftime('%Y-%m-%d')
        daily_logs.append(row_dict)

    return daily_logs
