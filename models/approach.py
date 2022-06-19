from models import db
from models.exercise import Exercise


class Approach(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	exercise = db.Column(db.String(80), db.ForeignKey(Exercise.name))
	repetitions = db.Column(db.Integer, nullable=False)
	weight = db.Column(db.Numeric(3,2), nullable=False)
