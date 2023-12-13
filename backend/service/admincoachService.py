from data.models import CoachExp
from flask import jsonify

def updateCV(coachexpID,visible):#updatecoachVisibility
    coach=CoachExp.query.filter_by(coachexpID=coachexpID).first()
    coach.update(coach.price,coach.rating,coach.experience,coach.bio,bool(visible))
    return jsonify(({"message": "coach visibility updated"}))