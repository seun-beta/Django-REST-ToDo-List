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
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            todo_item = serializer.save()
            todo_item.completed = False
            todo_item.url = reverse('todo_one', args=[todo_item.id], request=request)
            todo_item.save()
            return Response(serializer.data, status=201)
        return Response(None, status=400)


    def delete(self, request):
        ToDo.objects.all().delete()
        return Response(None, status=204)


class ToDoOne(APIView):
    def get(self, request, todo_id):
        try:
            todo = ToDo.objects.get(pk=todo_id)
            serializer = ToDoSerializer(todo)
            return Response(serializer.data, status=200)
        except ToDo.DoesNotExist:
            return Response(None, status=400)

    def patch(self, request, todo_id):
        try:    
            todo = ToDo.objects.get(pk=todo_id)
            serializer = ToDoSerializer(data=request.data, instance=todo, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(None, status=200)
        except ToDo.DoesNotExist:
            return Response(None, status=400)

    def delete(self, request, todo_id):
        try:
            todo = ToDo.objects.get(pk=todo_id)
            todo.delete()
            return Response(None, status=204)
        except ToDo.DoesNotExist:
            return Response(None, status=400)
