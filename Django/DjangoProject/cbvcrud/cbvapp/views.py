from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import StudentForm
from .models import Student
from django.views import View
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


# Create your views here.

def GreetUser(request):
    return HttpResponse('Changed Successfully')


class StudentGetPost(View):
    form_class = StudentForm
    template_name = 'student_form.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Values Saved Successfully')
        else:
            print('some fault')


class StudentUpdate(UpdateView):
    model = Student
    fields = ['name', 'roll']
    template_name = 'student_form.html'


class StudentDelete(DeleteView):
    template_name = 'student_confirm_delete.html'
    model = Student
    success_url = reverse_lazy('greet-user')


class StudentRetrieve(DetailView):
    print('here')
    model = Student
    fields = ['name', 'roll']


class StudentList(ListView):
    model = Student


fields = ['name', 'roll']