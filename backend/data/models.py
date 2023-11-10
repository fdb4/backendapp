from .exts import db
from uuid import uuid1

class Clients(db.Model):
    __tablename__="clients"
    clientID=db.Column(db.Integer,primary_key=True, autoincrement=True)
    email=db.Column(db.String(45), nullable=False, unique=True)
    password=db.Column(db.String(128), nullable=False)
    firstname=db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)
    workoutgoalID=db.Column(db.Integer, db.ForeignKey("workoutgoalID.workoutgoalID"))
    geninfoID=db.Column(db.Integer,db.ForeignKey("generalinfo.generalinfoID"))
    lastModified=db.Column(db.DateTime)
    

    def __repr__(self):
        return f"<Clients (self.firstname) >"
    
    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self,email, password, firstname, lastname):
        self.email = email
        self.pword = password
        self.firstname = firstname
        self.lastname = lastname

        db.session.commit()

class GeneralInfo(db.Model):
    __tablename__="generalinfo"
    geninfoID=db.Column(db.Integer,primary_key=True, unique=True)
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
    workoutgoalID=db.Column(db.Integer,primary_key=True, unique=True)
    cycling=db.Column(db.Integer)
    strength=db.Column(db.Integer)
    running= db.Column(db.Integer)
    sports=db.Column(db.Integer)
    yoga=db.Column(db.Integer)
    swimming=db.Column(db.Integer)
    martialarts=db.Column(db.Integer)
    other=db.Column(db.String(45))

    def __repr__(self):
        return f"<WorkoutGoal (self.firstname) >"

    def save(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()