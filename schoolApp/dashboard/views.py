from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'dashboard/students.html', {'students': students, 'school_name': 'DJango Learning School'})

def add_student(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        grade = request.POST['grade']
        Student.objects.create(name=name, age=age, grade=grade)
        return redirect('students')
    return render(request, 'dashboard/add_student.html')

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.age = request.POST['age']
        student.grade = request.POST['grade']
        student.save()
        return redirect('students')
    return render(request, 'dashboard/edit_student.html', {'student': student})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect('students')
