from django.urls import path

from . import views
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

urlpatterns = [
    path('', TaskList.as_view(), name='task'),
    path('task-create/',TaskCreate.as_view(), name='create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='delete'),

]