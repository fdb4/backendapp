from data.exts import db
from sqlalchemy.sql import text
from data.models import GeneralInfo, WorkoutGoal
from . import updateClientService
from flask import jsonify


def survey(clientID, height, weight, goalweight, movement, age, gender, cycling, strength, running, sports, yoga, swimming, martialarts, other):
    newGenInfo= GeneralInfo(
        geninfoID=clientID,
        height=height,
        weight=weight,
        goalweight=goalweight,
        movement=movement,
        age=age,
        gender=gender
    )

    newGenInfo.save()

    newWorkoutGoal = WorkoutGoal(
        workoutgoalID=clientID,
        cycling=cycling,
        strength=strength,
        running=running,
        sports=sports,
        yoga=yoga,
        swimming=swimming,
        martialarts=martialarts,
        other=other
    )

    newWorkoutGoal.save()

    updateClientService.updateClient(clientID=clientID, workoutGoalID=newWorkoutGoal.workoutgoalID, geninfoID=newGenInfo.geninfoID)
    return jsonify({"message": "Client preferences updated"})






    