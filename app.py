from flask import Flask, render_template, request
from api import api  

app = Flask(__name__)

@app.route("/")
def our_super_app():
    resultat=api.OpenFoodFactApi()
    products=resultat.getAll()

    # Flask utilise Jinja2 pour le templating
    return render_template("/flask.html",arg=products["products"])
                        