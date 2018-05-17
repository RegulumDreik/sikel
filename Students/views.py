from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import StudentModel


# Create your views here.
class list(View):

    def get(self, request, *args, **kwargs):
        students = StudentModel.objects.all()
        return render(request, 'list.html', {'students': students})