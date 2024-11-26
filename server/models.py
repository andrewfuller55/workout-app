from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!
class Workout(db.Model, SerializerMixin):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # add relationship
    user_plans = db.relationship('UserPlan', back_populates='workout', cascade='all, delete-orphan')

    # add serialization rules
    serialize_rules = ('-user_plans.workout',)

    def __repr__(self):
        return f"<Workout {self.name}>"


class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    # add relationship
    user_plans = db.relationship('UserPlan', back_populates='user', cascade='all, delete-orphan')

    # add serialization rules
    serialize_rules = ('-user_plans.user',)

    def __repr__(self):
        return f"<User {self.name}>"


class UserPlan(db.Model, SerializerMixin):
    __tablename__ = "user_plans"

    id = db.Column(db.Integer, primary_key=True)
    sets = db.Column(db.Integer, nullable=False)
    workout_id = db.Column(db.Integer, db.ForeignKey('workouts.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    # add relationships
    workout = db.relationship('Workout', back_populates = 'user_plans')
    user = db.relationship('User', back_populates = 'user_plans')
   

    # add serialization rules
    serialize_rules = ('-workout.user_plans', '-user.user_plans',)

    # add validation
    # @validates('price')
    # def validate_price(self, key, price):
    #     if not 1 <= price <= 30:
    #         raise ValueError('Price must between $1-30')
    #     return price

    def __repr__(self):
        return f"<UserPlan ${self.reps}>"
