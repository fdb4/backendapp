# service/client_service.py
from data.exts import db
from sqlalchemy.sql import text

def edit_client_profile(client_id, first_name, last_name, email, height, weight, goal_weight, movement_type, age, gender):
    # Update clients table
    client_query = text("""
        UPDATE clients 
        SET firstname = :first_name, lastname = :last_name, email = :email
        WHERE clientID = :client_id
    """)

    db.session.execute(client_query, {
        'first_name': first_name, 
        'last_name': last_name, 
        'email': email, 
        'client_id': client_id
    })

    # Update generalinfo table
    geninfo_query = text("""
        UPDATE generalinfo 
        SET height = :height, weight = :weight, goalweight = :goal_weight, 
            movement = :movement_type, age = :age, gender = :gender
        WHERE geninfoID = (
            SELECT geninfoID FROM clients WHERE clientID = :client_id
        )
    """)

    db.session.execute(geninfo_query, {
        'height': height, 
        'weight': weight, 
        'goal_weight': goal_weight, 
        'movement_type': movement_type, 
        'age': age, 
        'gender': gender, 
        'client_id': client_id
    })

    db.session.commit()