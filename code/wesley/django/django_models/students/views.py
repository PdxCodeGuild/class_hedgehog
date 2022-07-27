from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Student, Assignment

# Create your views here.
def index(request):

    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'students/index.html', context)

def detail(request, student_id):
    try:
        student = Student.objects.get(id = student_id)
    except Student.DoesNotExist:
        return redirect(reverse('students:index'))

    assignments = Assignment.objects.all() 
    context = {
        'student': student
    }

    return render(request, 'students/detail.html', context)

def update_student(request):
    if request.method == 'POST':
        form = request.POST
        assignment_id = form.get['assignment']
        student_id = form.get('student')

        try:
            student = Student.objects.get(id=student_id)
            assignment = Assignment.objects.get(id=assignment_id)
        except (Student.DoesNotExist, Assignment.DoesNotExist):
            return redirect(reverse('students:index'))

        student.assignments.add(assignment)
        student.save()
        return redirect(reverse('students:detail', arg=(student_id)))


