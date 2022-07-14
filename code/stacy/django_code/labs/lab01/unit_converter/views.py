from django.shortcuts import render, HttpResponse
from decimal import Decimal

# Create your views here.
def index(request):
    unit_conversions = {
        "ft": Decimal("0.3048"),
        "mi": Decimal("1609.34"),
        "m": Decimal("1"),      
        "km": Decimal("1000"),
        "yd": Decimal("0.9144"),
        "in": Decimal("0.0254")    
        } 
    measurement = Decimal(request.POST.get("measurement", 1))
    input_unit = request.POST.get("input_unit", "m")
    output_unit = request.POST.get("output_unit", "m")
    measurement_in_meters = 1
    converted_measurement = 1
    measurement_in_meters = measurement * unit_conversions.get(input_unit, 1)
    converted_measurement = measurement_in_meters / unit_conversions.get(output_unit, 1)
    context = {
        "measurement": measurement,
        "input_unit": input_unit,
        "output_unit": output_unit,
        "converted_measurement": converted_measurement
    }
    return render(request, 'unit_converter/index.html', context)

