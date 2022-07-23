from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    units= {'Feet': 0.3048, "Miles": 1609.34, "Meters": 1, "Kilometers": 1000}
    try:
        if request.method == 'POST':
            value = float(request.POST.get("value", 0.0))
            units_from = request.POST.get("units_from", "Meters")
            units_to = request.POST.get("units_to", "Meters")
#I hate this, but apparently list just wants to return a default of empty string:
            if units_to =="":
                units_to = "Meters"
            if units_from =="":
                units_from = "Meters"

            returned = (value * units[units_from]) / units[units_to]
            context = {"returned": returned, 'units_to' : units_to}
            return render(request, "unit_converter/index.html", context)
    except (ValueError, TypeError):
        
        return render(request, "unit_converter/index.html", {"error":"error"})
    return render(request, 'unit_converter/index.html')

