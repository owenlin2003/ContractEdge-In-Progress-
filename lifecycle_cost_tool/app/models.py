from app import db

class Contract(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.String(4), nullable=False)
    obligation_amount = db.Column(db.Float, nullable = False)
    description = db.Column(db.String(200), nullable = True)

    def __repr__(self):
        return f'<Contract {self.year} - ${self.obligation_amount}>'