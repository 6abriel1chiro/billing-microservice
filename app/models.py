from datetime import datetime
from app import db


# db = current_app.db  # Access the db object from the current app context


class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(100), nullable=False)
    concept = db.Column(db.String(100), unique=True, nullable=False)
    ammount = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def to_json(self):
        return {
            "id": self.id,
            "user_name": self.user_name,
            "concept": self.concept,
            "ammount": self.ammount,
            "date": self.date,
        }
