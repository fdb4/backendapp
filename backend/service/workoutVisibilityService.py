from data.models import Clients
from sqlalchemy.sql import text
from data.exts import db


def workoutVisibility(workoutID, visible):
    query = text(
        "update workoutbank set visible = :v where workoutID = :wid"
    )
    query = query.bindparams(v=visible, wid=workoutID)
    db.session.execute(query)
    db.session.commit()

    if visible == 1:
        return {"message": "Workout activated"}
    return {"message": "Workout de activated"}