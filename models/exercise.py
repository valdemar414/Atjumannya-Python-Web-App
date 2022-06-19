from models import db
from models.muscle import Muscle

class Exercise(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	muscle = db.Column(db.String(80), db.ForeignKey(Muscle.name))
