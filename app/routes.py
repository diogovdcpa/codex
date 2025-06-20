from flask import render_template
from . import db
from .models import Item
from flask import current_app as app

@app.route('/')
def index():
    items = Item.query.all()
    return render_template('index.html', items=items)
