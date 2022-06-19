from models import db
from models.exercise import Exercise
from models.user import User


class Approach(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	exercise = db.Column(db.String(80), db.ForeignKey(Exercise.name))
	user = db.Column(db.Integer, db.ForeignKey(User.id))
	repetitions = db.Column(db.Integer, nullable=False)
	weight = db.Column(db.Numeric(3,2), nullable=False)
