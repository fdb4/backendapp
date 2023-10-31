from flask_sqlalchemy import SQLAlchemy
from uuid import uuid1
db=SQLAlchemy()
class Clients(db.model):
    __table__="clients"
    client_id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(45))
    password=db.Column(db.String(45))
    coachID=db.Column(db.Integer)
    firstname=db.Column(db.String(45))
    lastname = db.Column(db.String(45))

