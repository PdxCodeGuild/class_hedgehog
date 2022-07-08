from flask import Flask, request, render_template
app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    unit_conversions = {
    "ft": 0.3048,
    "mi": 1609.34,
    "m": 1,
    "km": 1000,
    "yd": 0.9144,
    "in": 0.0254
    }
    distance=request.form.get("distance",0)
    input_unit=request.form.get("input_unit","m")
    output_unit=request.form.get("output_unit","m")
    message = ""
    converted_distance = 0
    try:
        distance = float(distance)
    except ValueError:
        message = "Distance must be a number. "
        distance = 0.0
    
    if unit_conversions.get(input_unit) == None:
        message += "Invalid input unit. "
        input_unit = "m"
    if unit_conversions.get(output_unit) == None:
        message += "Invalid output unit. "
        output_unit = "m"

    distance_in_meters = distance * unit_conversions.get(input_unit)
    converted_distance = distance_in_meters / unit_conversions.get(output_unit)

    return render_template("index.html", message=message, distance=distance, input_unit=input_unit, output_unit=output_unit, converted_distance=converted_distance)

app.run(debug=True)
