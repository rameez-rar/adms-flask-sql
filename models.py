from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Pet(db.Model):
    __tablename__ = 'pets'  # Optional: specify the table name explicitly

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    type = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Pet {self.name}, Age: {self.age}, Type: {self.type}>'
