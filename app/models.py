from app import db
from datetime import datetime



class Phone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phonenumber = db.Column(db.String(50), nullable=False, unique=True)
    address = db.Column(db.String(10000), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        db.session.add(self)
        db.session.commit()

   
