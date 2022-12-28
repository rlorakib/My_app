from django.shortcuts import render
from django.http import HttpResponse
from .models import student
from my_app import forms
# Create your views here.

def index(request):
    student_list = student.objects.order_by('name')
    diction= {'student':student_list}
    return render(request, 'my_app/index.html', context=diction)


def form(request):
    new_form = forms.StudentForm()

    if request.method == "POST":
        new_form = forms.StudentForm(request.POST)

        if new_form.is_valid():
            new_form.save(commit=True)
            return index(request)

    diction = {'form':new_form}
    return render(request,'my_app/form.html', context=diction)