from exts import db
from uuid import uuid1


class Clients(db.Model):
    client_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), nullable=False)
    password = db.Column(db.String(45), nullable=False)
    coachID = db.Column(db.Integer)
    firstname = db.Column(db.String(45), nullable=False)
    lastname = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return f"<Clients (self.title) >"

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, email, password, firstname, lastname):
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname