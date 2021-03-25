from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def our_super_app():
    # Flask utilise Jinja2 pour le templating
    return render_template("/flask.html")
                        