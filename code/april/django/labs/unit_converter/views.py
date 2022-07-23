from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    convert = {
        'feet': 0.3048,
        'miles': 1609.34,
        'meters': 1,
        'kilometers': 1000,
        'yards': 0.9144,
        'inches': 0.0254
    }

    quantity = float(request.POST.get('quantity', 0))

    unit_name = request.POST.get('unit_name', 'feet')

    unit = convert[unit_name]
    
    total = quantity * unit

    converted_amt = round(total, 4)

    context = {
        "converted_amt": converted_amt,
        "quantity": quantity,
        "unit_name": unit_name
    }


    return render(request, 'unit_converter/index.html', context)
