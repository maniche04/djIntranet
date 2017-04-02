from django.conf.urls import url, include
from tasks import views
from rest_framework import routers, serializers, viewsets
from tasks.serializers import ProjectViewSet, StateViewSet

# 'Projects'
# -----------
projectRouter = routers.DefaultRouter()
projectRouter.register(r'projects', ProjectViewSet)

# 'States'
# -----------
stateRouter = routers.DefaultRouter()
stateRouter.register(r'states',StateViewSet)

app_name = 'auth'

urlpatterns = [
    url(r'^', include(projectRouter.urls)),
    url(r'^', include(stateRouter.urls)),
    url(r'^list/', views.listTasks.as_view()),
    url(r'^add/',views.addTask.as_view()),
    url(r'^get/(?P<task_id>\d+)/$', views.fetchTask),
    url(r'^delete/(?P<task_id>\d+)', views.deleteTask.as_view()),
    url(r'^(?P<task_id>\d+)/subtasks/list/', views.listSubTasks.as_view()),
    url(r'^subtasks/add/', views.addSubTask.as_view()),
    url(r'^subtasks/get/(?P<subtask_id>\d+)/$', views.fetchSubTask.as_view()),
    url(r'^subtasks/delete/(?P<subtask_id>\d+)/$', views.deleteSubTask.as_view()),
    url(r'^subtasks/(?P<subtask_id>\d+)/activities/list/', views.listActivities.as_view()),
    url(r'^activities/add/', views.addActivity.as_view()),
    url(r'^activities/start/(?P<activity_id>\d+)', views.startActivity.as_view()),
    url(r'^activities/update/(?P<activity_id>\d+)', views.updateActivity.as_view()),
    url(r'^activities/delete/(?P<activity_id>\d+)', views.deleteActivity.as_view()),
    url(r'^activities/running/', views.runningActivity.as_view()),
]