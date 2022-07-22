from flask import Flask, request, render_template
from decimal import Decimal

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    unit_conversions = {
    "ft": Decimal(0.3048),
    "mi": Decimal(1609.34),
    "m": Decimal(1),
    "km": Decimal(1000),
    "yd": Decimal(0.9144),
    "in": Decimal(0.0254)
    }
    distance=Decimal(request.form.get("distance",1))
    print(type(distance))
    input_unit=request.form.get("input_unit","m")
    output_unit=request.form.get("output_unit","m")
    message = ""
    distance_in_meters = 1
    converted_distance = 1
    # try:
    #     distance = Decimal(distance)
    # except ValueError:
    #     message = "Distance must be a number. "
    #     distance = Decimal(1)
    
    # if unit_conversions.get(input_unit) == None:
    #     message += "Invalid input unit. "
    #     input_unit = "m"
    # if unit_conversions.get(output_unit) == None:
    #     message += "Invalid output unit. "
    #     output_unit = "m"

    distance_in_meters = distance * unit_conversions.get(input_unit, 1)
    print(type(distance_in_meters))
    converted_distance = distance_in_meters / unit_conversions.get(output_unit, 1)
    print(type(converted_distance))
    return render_template("index.html", message=message, distance=distance, input_unit=input_unit, output_unit=output_unit, converted_distance=converted_distance)

app.run(debug=True)
