from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from .models import Student
from .forms import StudentForm

class StudentListView(View):
    def get(self, request):
        students = Student.objects.all()
        return render(request, 'students/student_list.html', {'students': students})

class StudentCreateView(View):
    def get(self, request):
        form = StudentForm()
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student_list')
        return render(request, 'students/student_form.html', {'form': form})

class StudentUpdateView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(instance=student)
        return render(request, 'students/student_form.html', {'form': form})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully!")
            return redirect('student_list')
        return render(request, 'students/student_form.html', {'form': form})

class StudentDeleteView(View):
    def get(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        return render(request, 'students/student_confirm_delete.html', {'student': student})

    def post(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        student.delete()
        messages.success(request, "Student deleted successfully!")
        return redirect('student_list')

