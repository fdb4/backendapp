# filterCoachesByGoalsService.py
from data.exts import db
from sqlalchemy.sql import text


def filter_coaches_by_goal(goal_type):
   valid_goals = ['cycling', 'strength', 'running', 'sports', 'yoga', 'swimming', 'martialarts']
   if goal_type not in valid_goals:
       return []  


   query = text(
   "SELECT c.clientID, c.email, c.firstname, c.lastname, ce.price, ce.rating, ce.experience, ce.bio, l.gym, l.town, s.state, "
   "wg.cycling, wg.strength, wg.running, wg.sports, wg.yoga, wg.swimming, wg.martialarts, wg.other "
   "FROM clients c "
   "JOIN coachexp ce ON c.coachexpID = ce.coachexpID "
   "JOIN workoutgoal wg ON c.workoutgoalID = wg.workoutgoalID "
   "JOIN location l ON ce.locationID = l.locationID "
   "JOIN state s ON l.stateID = s.stateID "
   "WHERE wg.{} = 1".format(goal_type))


   results = db.session.execute(query).fetchall()
   return (results)