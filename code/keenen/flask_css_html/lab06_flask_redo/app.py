from lib2to3.pytree import convert
from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    conversions = {
        "ft": 0.3048,
        "mi": 1609.34,
        "m": 1,
        "km": 1000,
        'yd': 0.9144,
        'in': 0.0254,
    }
    
    distance = request.form.get("distance",0)
    if distance == '':
        distance = 0
    distance = float(distance)
   
    unit_input = request.form.get('unit_input')
    unit_output = request.form.get('unit_output')

    if unit_input != None:
        input = conversions.get(unit_input)
        output = conversions.get(unit_output)
        distance_converted = (distance * input) / output 
        distance_converted = round(distance_converted, 2)
    else:
        unit_input = 'ft'
        distance_converted = 0

    if unit_output == None:
        unit_output = 'ft'

    return render_template("index.html", distance=distance, distance_selected=distance_converted, unit_input=unit_input, unit_output=unit_output)
    
app.run(debug=True)

