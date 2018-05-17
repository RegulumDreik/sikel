from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .models import StudentModel
from .forms import StudentForm


# Create your views here.
class List(View):

    def get(self, request, *args, **kwargs):
        students = StudentModel.objects.all()
        return render(request, 'list.html', {'students': students})


class Add(View):
    adding_form = StudentForm()

    def get(self, request):
        return render(request, 'add.html', {'form': self.adding_form})

    def post(self, request):
        self.adding_form=StudentForm(request.POST)
        if self.adding_form.is_valid():
            self.adding_form.save(True)
            return HttpResponseRedirect('/student/list')
        else:
            self.adding_form.clean()
        return render(request, 'add.html', {'form': self.adding_form})
