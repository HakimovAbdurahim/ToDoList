from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class TaskList(ListView):
    model = Task
    template_name = 'task_list.html'
    # context_object_name = 'task'


class TaskDetail(DetailView):
    model = Task
    template_name = 'task_detail.html'


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    # fields = ['title', 'description']
    success_url = reverse_lazy('task')
    template_name = 'task_form.html'


class TaskUpdate(UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy('task')
    template_name = 'task_form.html'


class TaskDelete(DeleteView):
    model = Task
    success_url = reverse_lazy('task')
    template_name = 'task_confirm_delete.html'
