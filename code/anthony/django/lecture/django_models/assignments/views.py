from django.http import HttpResponse
from django.shortcuts import render
from .models import Assignment


def index(request):
    assignments = Assignment.objects.all()

    context = {
        'assignments': assignments
    }
    return render(request, 'assignments/index.html', context)
