from CommandHandler import CommandHandler
from Weapon import Weapon
from flask import Flask
from flask import json
from main import weapon_generation
app = Flask(__name__, static_url_path='/static/')

def json_type_response(value):
        return app.response_class(
        response = value,
        status = 200,
        mimetype='application/json'
    )


@app.route('/')
def index():
    return app.send_static_file('help.html')

@app.route('/assault_rifle')
def assault_rifle():
    w = Weapon()
    w.generate("ASSAULT_RIFLE")
    return json_type_response(json.dumps(w.__dict__))

@app.route('/shotgun')
def shotgun():
    w = Weapon()
    w.generate("SHOTGUN")
    return json_type_response(json.dumps(w.__dict__))

@app.route('/sniper_rifle')
def sniper():
    w = Weapon()
    w.generate("SNIPER_RIFLE")
    return json_type_response(json.dumps(w.__dict__))

@app.route('/assault_rifle/<number>')
def assault_rifle_multiple(number):
    number = int(number)
    weapon_list = []
    for i in range(number):
        w = Weapon()
        weapon_list.append(w)
        weapon_list[i].generate("ASSAULT_RIFLE")
    return json_type_response(json.dumps([w.__dict__ for weapon_list in weapon_list]))

@app.route('/shotgun/<number>')
def shotgun_multiple(number):
    number = int(number)
    weapon_list = []
    for i in range(number):
        w = Weapon()
        weapon_list.append(w)
        weapon_list[i].generate("SHOTGUN")
    return json_type_response(json.dumps([w.__dict__ for weapon_list in weapon_list]))

@app.route('/sniper_rifle/<number>')
def sniper_rifle_multiple(number):
    number = int(number)
    weapon_list = []
    for i in range(number):
        w = Weapon()
        weapon_list.append(w)
        weapon_list[i].generate("SNIPER_RIFLE")
    return json_type_response(json.dumps([w.__dict__ for weapon_list in weapon_list]))
