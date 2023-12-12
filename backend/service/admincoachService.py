from data.models import CoachExp
from flask import jsonify
from sqlalchemy.sql import text
from data.exts import db

def updateCV(coachexpID,visible):#updatecoachVisibility
    coach=CoachExp.query.filter_by(coachexpID=coachexpID).first()

    coach.update(coach.price,coach.rating,coach.experience,coach.bio,visible)

    if visible == 1:
        query = text(
            "update clients set coachexpid = NULL, isCoach = 0 where coachexpid = :cid "
        )
        query = query.bindparams(cid=coachexpID)
        db.session.execute(query)

        query = text(
            "delete from coachexp where coachexpid = :cid "
        )
        query = query.bindparams(cid=coachexpID)
        db.session.execute(query)

        db.session.commit()

    return jsonify(({"message": "coach visibility updated"}))