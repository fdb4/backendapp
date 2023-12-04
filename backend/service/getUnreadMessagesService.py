from data.exts import db
from sqlalchemy.sql import text

# service/message_service.py

def get_unread_message_count(user_id):
    query = text("""
    SELECT COUNT(*) 
    FROM messagetable
    WHERE (clientID = :user_id OR clientID2 = :user_id) AND MRead = 0
    """)

    result = db.session.execute(query, {'user_id': user_id}).fetchone()
    db.session.commit()

    # Return the count of unread messages
    return result[0]  