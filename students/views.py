from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")



def students_lists(request):
    students = Student.objects.all()        #frontend ma falne

    return render(
        request,
        "students/students_lists.html",
        {"students": students}
    )



def student_create(request):

    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()                           #form save vayexi matrai gayera database ma basxa
            return redirect("students_lists")       # vereko xa vane front end ma faldinxa

    else:
        form = StudentForm()                     # khali form deko

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )

from django.shortcuts import get_object_or_404
def student_update(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        form = StudentForm(
            request.POST,
            instance=student      #data k xa avnera tanera rakheko.
        )

        if form.is_valid():
            form.save()
            return redirect("students_lists")

    else:
        form = StudentForm(instance=student)

    return render(
        request,
        "students/student_form.html",
        {"form": form}
    )

def student_delete(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":
        student.delete()
        return redirect("students_lists")

    return render(
        request,
        "students/student_confirm_delete.html",
        {"student": student}
    )
def register(request):

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = UserCreationForm()

    return render(
        request,
        "registration/register.html",
        {"form": form}
    )