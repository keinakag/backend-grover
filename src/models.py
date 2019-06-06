from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(8), unique=True, nullable=False)
    birthday = db.Column(db.String(8), unique=True, nullable=False)
    gender = db.Column(db.String(10), unique=True, nullable=False)


    def __repr__(self):
        return '<Person %r>' % self.username

    def serialize(self):
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password,
            "birthday": self.birthday,
            "gender": self.gender
        }