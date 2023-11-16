from .exts import db
from uuid import uuid1
import datetime

class Clients(db.Model):
    __tablename__="clients"
    clientID=db.Column(db.Integer(),primary_key=True, autoincrement=True)
    email=db.Column(db.String(45), nullable=False, unique=True)
    password=db.Column(db.String(128), nullable=False)
    firstname=db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    workoutgoalID=db.Column(db.Integer(), db.ForeignKey("workoutgoal.workoutgoalID"))
    geninfoID=db.Column(db.Integer(),db.ForeignKey("generalinfo.geninfoID"))
    coachexpID=db.Column(db.Integer(),db.ForeignKey("coachexp.coachexpID"))
    lastmodified=db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    

    def __repr__(self):
        return f"<Clients (self.firstname) >"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,email, password, firstname, lastname, workoutGoalID, geninfoID, coachexpID):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.workoutgoalID = workoutGoalID
        self.geninfoID = geninfoID
        self.coachexpID = coachexpID

        db.session.commit()

class GeneralInfo(db.Model):
    __tablename__="generalinfo"
    geninfoID=db.Column(db.Integer(),primary_key=True, unique=True)
    height=db.Column(db.Double, nullable=False, unique=True)
    weight=db.Column(db.Double, nullable=False)
    goalweight=db.Column(db.Integer, nullable=False)
    movement = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"<GeneralInfo (self.firstname) >"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class WorkoutGoal(db.Model):
    __tablename__="workoutgoal"
    workoutgoalID=db.Column(db.Integer(),primary_key=True, unique=True)
    cycling=db.Column(db.SmallInteger)
    strength=db.Column(db.SmallInteger)
    running= db.Column(db.SmallInteger)
    sports=db.Column(db.SmallInteger)
    yoga=db.Column(db.SmallInteger)
    swimming=db.Column(db.SmallInteger)
    martialarts=db.Column(db.SmallInteger)
    other=db.Column(db.String(45))

    def __repr__(self):
        return f"<WorkoutGoal (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class CoachExp(db.Model):
    __tablename__="coachexp"
    coachexpID=db.Column(db.Integer(),primary_key=True, unique=True)
    price=db.Column(db.Double)
    rating=db.Column(db.SmallInteger())
    locationID= db.Column(db.Integer(), db.ForeignKey("workoutgoal.workoutgoalID"))
    experience=db.Column(db.Date)
    bio=db.Column(db.Text)
    lastmodified=db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    

    def __repr__(self):
        return f"<CoachExp (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class Location(db.Model):
    __tablename__="location"
    locationID=db.Column(db.Integer(),primary_key=True, unique=True)
    gym=db.Column(db.String(45))
    town=db.Column(db.String(45))
    stateID= db.Column(db.Integer(), db.ForeignKey("state.stateID"))
    lastmodified=db.Column(db.DateTime,  default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<Location (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class State(db.Model):
    __tablename__="state"
    stateID=db.Column(db.Integer(),primary_key=True, unique=True)
    state=db.Column(db.String(45))

    def __repr__(self):
        return f"<State (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

class ClientCoaches(db.Model):
    __tablename__="clientcoaches"
    requestID=db.Column(db.Integer(),primary_key=True, unique=True)
    clientID=db.Column(db.Integer(), db.ForeignKey("clients.clientID"))
    request=db.Column(db.SmallInteger)
    coachexpID=db.Column(db.Integer(),db.ForeignKey("coachexp.coachexpID"))
    lastmodified=db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f"<ClientCoaches (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()