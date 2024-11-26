#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Workout, User, UserPlan

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")
        # Seed code goes here!
        # This will delete any existing rows
        # so you can run the seed file multiple times without having duplicate entries in your database
        print("Deleting data...")
        User.query.delete()
        Workout.query.delete()
        UserPlan.query.delete()

        print("Creating Workouts...")
        workout1 = Workout(name="Squats")
        workout2 = Workout(name="Pull ups")
        workout3 = Workout(name="Push ups")
        workouts = [workout1, workout2, workout3]

        print("Creating users...")

        user1 = User(name="Andrew Fuller")
        user2 = User(name="Roni Coleman")
        user3 = User(name="Arnold Schwarzenegger")
        users = [user1, user2, user3]

        print("Creating UserPlan...")

        plan1 = UserPlan(workout=workout1, user=user1, sets=4)
        plan2 = UserPlan(workout=workout2, user=user2, sets=7)
        plan3 = UserPlan(workout=workout3, user=user3, sets=7)
        userPlans = [plan1, plan2, plan3]
        db.session.add_all(workouts)
        db.session.add_all(users)
        db.session.add_all(userPlans)
        db.session.commit()

        print("Seeding done!")