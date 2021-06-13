from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ToDo
from .serializers import ToDoSerializer


class ToDoList(APIView):
    def post(self, request):
        todo = ToDoSerializer(request.data)
        return Response(todo.data)

class ToDoOne(APIView):
    pass