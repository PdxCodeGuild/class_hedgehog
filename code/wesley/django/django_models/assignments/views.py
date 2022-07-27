from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Assignment
from .forms import NewAssignmentForm


# Create your views here.

def index(request):
    assignments = Assignment.objects.all().order_by('date_due')

    context = {
        'assignments': assignments
    }
    return render(request, 'assignments/index.html', context)

def create_assignment(request):
    if request.method == 'POST':
        form = NewAssignmentForm(request.POST)
        if form.is_valid():
            assignment = Assignment()
            assignment.title = form.cleaned_data['title']
            assignment.description = form.cleaned_data['description']
            if form.cleaned_data['date_assigned']:
                assignment.date_assigned = form.cleaned_data['date_assigned']
            if form.cleaned_data['date_due']:
                assignment.date_due = form.cleaned_data['date_due']

            assignment.save()

            return redirect(reverse('assignment:index')) 
        else:
            context = {
                'form': form
            }
            return render(request, 'assignments/create.html', context)


    context = {
        'form': NewAssignmentForm()
    }
    return render(request, 'assignments/create.html', context)
