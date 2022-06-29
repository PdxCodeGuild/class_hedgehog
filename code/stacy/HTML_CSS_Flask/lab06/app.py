from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return f'''
Welcome to unit converter!
Please enter the distance you want to convert followed by the input unit and output unit.
For example, the route should look as follows:
/convert/10/mi/ft.

Supported units are as follows.
in:  inches,
ft:  feet,
yd:  yards,
mi:  miles,
m:   meters,
km:  kilometers
'''

# @app.route("/convert/<int:distance>/<string:unit>")
# def convert_to_meters(distance: int, unit: str): 
#     unit_conversions = {
#     "ft": 0.3048,
#     "mi": 1609.34,
#     "m": 1,
#     "km": 1000
#     }
#     distance_in_meters = distance * unit_conversions.get(unit)
#     return f'{distance} {unit} is {distance_in_meters} m'
    
@app.route("/convert/<int:distance>/<string:input_unit>/<string:output_unit>")
def convert_to_meters(distance: int, input_unit: str, output_unit: str): 
    unit_conversions = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
    }
    distance_in_meters = distance * unit_conversions.get(input_unit)
    converted_distance = distance_in_meters / unit_conversions.get(output_unit)
    return f'{distance} {input_unit} is {converted_distance} {output_unit}'
    
app.run(debug=True)
