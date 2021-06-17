from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import ToDo
from .serializers import ToDoSerializer
from todo import serializers


class ToDoList(APIView):

    def get(self, request):
        todos = ToDo.objects.all()
        todo_data = ToDoSerializer(todos, many=True)
        return Response(todo_data.data)

    def post(self, request):
        todo = ToDoSerializer(data=request.data)
        if todo.is_valid():
            todo_item = todo.save()
            todo_item.completed = False
            todo_item.url = reverse('todo_one', args=[todo_item.id], request=request)
            todo_item.save()
        return Response(todo.data)

    def delete(self, request):
        ToDo.objects.all().delete()
        return Response(None)


class ToDoOne(APIView):
    def get(self, request, todo_id):
        todo = ToDo.objects.get(pk=todo_id)

        serializer = ToDoSerializer(todo)
        return Response(serializer.data)