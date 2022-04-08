from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List':'/todos/',
        'Detail View':'/task-detail/<str:pk>',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>',
        'Delete':'/task-delete/<str:pk>',
    }
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    todos = Todo.objects.all()
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data)