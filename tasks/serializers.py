from tasks.models import Task, Project, State, SubTask, ActivityLog
from rest_framework import serializers, viewsets

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TaskReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        depth = 1
        fields = '__all__'

# PROJECT
#---------
class ProjectSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Project
        fields = ('id','title','description')

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

# STATE
#------
class StateSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = State
        fields = ('id','state','description')

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

# SUB-TASK
#---------
class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'

class SubTaskViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = SubTaskSerializer

# ACTIVITY
# ---------
class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        fields = '__all__'

class ActivityReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityLog
        depth = 3
        fields = '__all__'

## JESUS DEL POZO EDT 100 ML
