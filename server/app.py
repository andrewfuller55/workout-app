#!/usr/bin/env python3

# Standard library imports

# Remote library imports
from flask import request, jsonify, request, make_response
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import *
# Add your model imports


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

class Workouts(Resource):

    def get(self):
        workouts = [workout.to_dict(rules=('-user_plans',)) for workout in Workout.query.all()]
        return make_response(jsonify(workouts), 200)

api.add_resource(Workouts, '/workouts')


class WorkoutByID(Resource):

    def get(self, id):

        workout = Workout.query.filter_by(id=id).first()
        
        if workout:
            return workout.to_dict(), 200
        else:
            return make_response({"error": "Workout not found"}, 404)
    
    def delete(self, id):

        workout = Workout.query.filter_by(id=id).first()
        
        if not workout:
            return make_response({"error": "Workout not found"}, 404)
        
        db.session.delete(workout)
        db.session.commit()

        return {}, 204


api.add_resource(WorkoutByID, '/workouts/<int:id>')


class Users(Resource):

    def get(self):
        users = [user.to_dict(rules=('-user_plans',)) for user in User.query.all()]
        return make_response(jsonify(users), 200)

api.add_resource(Users, '/users')


class UserPlans(Resource):

    def post(self):


        try:
            data = request.get_json()

            new_obj = UserPlan(
                sets=data['sets'],
                user_id=data['user_id'],
                workout_id=data['workout_id'],
            )

            db.session.add(new_obj)
            db.session.commit()

            return make_response(new_obj.to_dict(), 201)
        except ValueError:
            return make_response({"errors": ["validation errors"]}, 400)
    

api.add_resource(UserPlans, '/user_plans')

if __name__ == '__main__':
    app.run(port=5555, debug=True)

