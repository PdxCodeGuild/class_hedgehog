from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from .models import Assignment
from .forms import NewAssignmentForm


def index(request):
    assignments = Assignment.objects.all().order_by('date_due')
    date = timezone.now()

    context = {
        'assignments': assignments,
        'date': date
    }
    return render(request, 'assignments/index.html', context)


def create_assignment(request):
    # POST
    if request.method == "POST":
        form = NewAssignmentForm(request.POST)
        if form.is_valid():
            assignment = Assignment()
            assignment.title = form.cleaned_data['title']
            assignment.description = form.cleaned_data['description']

            date_assigned = form.cleaned_data['date_assigned']
            date_due = form.cleaned_data['date_due']

            if date_assigned:
                assignment.date_assigned = date_assigned
            if date_due:
                assignment.date_due = date_due

            assignment.save()
            url = reverse('assignments:index')
            return redirect(url)
        else:
            context = {
                'form': form
            }
            return render(request, 'assignments/create.html', context)

    # GET

    context = {
        'form': NewAssignmentForm()
    }
    return render(request, 'assignments/create.html', context)
