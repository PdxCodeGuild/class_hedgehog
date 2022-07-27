from django.shortcuts import redirect, render
from .models import Student
from django.urls import reverse
from assignments.models import Assignment
# Create your views here.


def index(request):
    students = Student.objects.all()

    context = {
        'students': students
    }

    return render(request, 'students/index.html', context)

# Read
def detail(request, student_id):
    try:
        student = Student.objects.get(id=student_id)
    except Student.DoesNotExist:
        return redirect(reverse('students:index'))
    
    assignments = Assignment.objects.all()
    context = {
        'student': student,
        'assignments': assignments
    }
    return render(request, 'students/detail.html', context)

def update_student(request):
    if request.method == 'POST':
        form = request.POST
        assignment_id = form.get('assignment')
        student_id = form.get('student')

        try:
            student = Student.objects.get(id=student_id)
            assignment = Assignment.objects.get(id=assignment_id)
        except (Student.DoesNotExist, Assignment.DoesNotExist):
            return redirect(reverse('students:index'))

        student.assignments.add(assignment)
        student.save()

        return redirect(reverse('students:detail', args=(student_id,)))
    return redirect(reverse('students:index'))