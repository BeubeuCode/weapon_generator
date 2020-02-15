from CommandHandler import CommandHandler
from Weapon import Weapon
from flask import Flask
from flask import json
from main import weapon_generation
app = Flask(__name__, static_url_path='/static/')

def create_json_resp(w: Weapon):
    response = app.response_class(
        response = w.generate_json(),
        status = 200,
        mimetype='application/json'
    )
    return response

@app.route('/')
def index():
    return app.send_static_file('help.html')

@app.route('/assault_rifle')
def assault_rifle():
    w = Weapon()
    w.generate("ASSAULT_RIFLE")
    return create_json_resp(w)

@app.route('/shotgun')
def shotgun():
    w = Weapon()
    w.generate("SHOTGUN")
    return create_json_resp(w)

@app.route('/sniper_rifle')
def sniper():
    w = Weapon()
    w.generate("SNIPER_RIFLE")
    return create_json_resp(w)