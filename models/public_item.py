from models import db

class PublicItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    color = db.Column(db.String(80), unique=False, nullable=False)

    def __repr__(self):
        return f"<PublicItem {self.name}>"
