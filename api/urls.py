from django.urls import path
from . import views

urlpatterns =[
path('',views.apiOverview,name='api-overview'),
path('todos/',views.taskList,name='todo-list'),
path('todos/<str:pk>',views.todoDetail,name='todo-deatil'),
path('todos-create/',views.todoCreate,name='todo-create'),
path('todos-update/<str:pk>',views.todoUpdate,name='todo-update'),
path('todos-delete/<str:pk>',views.todoDelete,name='todos-delete'),
path('upload/CSOfile',views.CSOUploadView.as_view(), name='organization-upload-excel'),
]