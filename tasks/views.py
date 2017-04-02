from django.shortcuts import render
from tasks.models import Task, SubTask, ActivityLog
from tasks.serializers import TaskSerializer, TaskReadSerializer, SubTaskSerializer, ActivitySerializer, ActivityReadSerializer
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.views import APIView

# Create your views here.
class listTasks(APIView):
    def get(self, request,  format = None):
        tasks = Task.objects.all()
        serializer = TaskReadSerializer(tasks, many = True)
        return Response(serializer.data)

class addTask(APIView):
    def post(self, request, format = None):
        serializer = TaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(createdBy = request.user, modifiedBy = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class addSubTask(APIView):
    def post(self, request, format = None):
        serializer = SubTaskSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(owner = request.user, createdBy = request.user, modifiedBy = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class addActivity(APIView):
    def post(self, request, format = None):
        serializer = ActivitySerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(createdBy = request.user, modifiedBy = request.user)
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class updateActivity(APIView):
    def post(self, request, activity_id):
        activity = ActivityLog.objects.get(id = activity_id)
        serializer = ActivitySerializer(activity, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save(modifiedBy=request.user, endtime = request.data['endtime'], description = request.data['description'])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class deleteTask(APIView):
    def get(self, request, task_id):
        task = Task.objects.get(id = task_id)
        task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class deleteSubTask(APIView):
    def get(self, request, subtask_id):
        subtask = SubTask.objects.get(id = subtask_id)
        subtask.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class deleteActivity(APIView):
    def get(self, request, activity_id):
        activty = ActivityLog.objects.get(id = activity_id)
        activty.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

class startActivity(APIView):
    def post(self, request, format = None):
        return Response(1);

class stopActivity(APIView):
    def post(self, request, format = None):
        return Response(0);

class runningActivity(APIView):
    def get(self, request, format = None):
        try:
            activity = ActivityLog.objects.get(endtime__isnull = True)
        except:
            activity = None
        serializer = ActivityReadSerializer(activity)
        return Response(serializer.data)

def fetchTask(request, task_id):
    task = Task.objects.get(id=task_id)
    serializer = TaskReadSerializer(task)
    return JsonResponse(serializer.data, safe = False)

class listSubTasks(APIView):
    def get(self, request, task_id):
        subtasks = SubTask.objects.filter(task = task_id)
        serializer = SubTaskSerializer(subtasks, many = True)
        return Response(serializer.data)

class listActivities(APIView):
    def get(self, request, subtask_id):
        activities = ActivityLog.objects.filter(subtask = subtask_id).order_by('-id')
        serializer = ActivitySerializer(activities, many = True)
        return Response(serializer.data)

class fetchSubTask(APIView):
    def get(self, request, subtask_id):
        subtask = SubTask.objects.get(id = subtask_id)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)
