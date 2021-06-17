from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoList(APIView):

    def get(self, request):
        return Response(None)

    def post(self, request):
        todo = ToDoSerializer(data=request.data)
        if todo.is_valid():
            todo.save()
        return Response(todo.data)

    def delete(self, request):
        return Response(None)


class ToDoOne(APIView):
    pass