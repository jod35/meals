from flask_restx import Api,Resource,marshal,fields
from flask import Blueprint,jsonify,request
from .models import Meal
from .exts import db


api_bp=Blueprint('api',__name__)

api=Api(api_bp)

#serialization model

model=api.model(
    'Meal',
    {
        "id":fields.Integer(),
        "name":fields.String(),
        "price":fields.Integer(),
        "description":fields.String()
    })

@api.route('/meals')
class MealResource(Resource):
    #get all meals
    def get(self):
        meals=Meal.get_meals_descending()

        return marshal(meals,fields=model,envelope="meals")
    #create a new meal resource
    def post(self):
        data=request.get_json()

        new_meal=Meal(name=data.get('name'),price=data.get('price'),description=data.get('description'))

        new_meal.save()

        return marshal(new_meal,fields=model,envelope="meal")


@api.route('/meal/<int:id>')
class MealResourceID(Resource):
    #get a resource by id
    def get(self,id):
        meal=Meal.get_by_id(id)

        return marshal(meal,fields=model,envelope="meal")
    #update a resource by id
    def put(self,id):
        meal=Meal.get_by_id(id)

        data=request.get_json()

        meal.name=data.get('name')

        meal.price=data.get('price')

        meal.description=data.get('description')

        db.session.commit()

        return marshal(meal,fields=model,envelope="meal")
    # delete a resource by its id
    def delete(self,id):
        meal=Meal.get_by_id(id)
        meal.delete()
        return marshal(meal,fields=model,envelope="meal")




