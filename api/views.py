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
        'Detail View':'/todos/<str:pk>',
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

@api_view(['GET'])
def todoDetail(request,pk):
    todos = Todo.objects.get(id=pk)
    serializer = TodoSerializer(todos,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def todoCreate(request):
    serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['POST'])
def todoUpdate(request,pk):
    todo = Todo.objects.get(id=pk)

    serializer = TodoSerializer(instance=todo,data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def todoDelete(request,pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    
    return Response("Item Deleted successfully")

