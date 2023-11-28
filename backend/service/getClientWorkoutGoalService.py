from data.models import Clients, WorkoutGoal
from data.exts import db
def getClientWorkoutGoal(clientID):
    general_info=db.session.query(
        Clients.clientID,
        Clients.firstname, 
        Clients.lastname, 
        Clients.email,
        WorkoutGoal.cycling,
        WorkoutGoal.running,
        WorkoutGoal.strength,
        WorkoutGoal.running,
        WorkoutGoal.sports,
        WorkoutGoal.yoga,
        WorkoutGoal.swimming,
        WorkoutGoal.martialarts,
        WorkoutGoal.other
    ).join(Clients, (Clients.clientID == clientID) & (WorkoutGoal.workoutgoalID == Clients.workoutgoalID)).all()
    return general_info