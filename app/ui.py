from flask import Blueprint,render_template
from .models import Meal


ui_bp=Blueprint('ui_bp',__name__)

@ui_bp.route('/')
def index():
    meals=Meal.get_all()
    return render_template('index.html',meals=meals)
