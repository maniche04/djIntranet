from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    color = models.CharField(max_length = 200)

class Team(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

class Tag(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()

class State(models.Model):
    state = models.CharField(max_length=100)
    description = models.TextField()

class Task(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    project = models.ForeignKey(Project, null = True, on_delete = models.SET_NULL)
    state = models.ForeignKey(State, null = True, on_delete = models.SET_NULL)
    dueBy = models.DateTimeField()
    plannedStart = models.DateTimeField()
    startedAt = models.DateTimeField(null = True)
    completedAt = models.DateTimeField(null = True)
    remarks = models.TextField(null = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(User, related_name= 'taskCreatedBy', null = True, on_delete = models.SET_NULL)
    modifiedAt = models.DateTimeField(auto_now = True)
    modifiedBy = models.ForeignKey(User, related_name = 'taskModifiedBy', null = True, on_delete = models.SET_NULL)

class SubTask(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    title = models.CharField(max_length = 2000)
    description = models.TextField()
    owner = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)
    state = models.ForeignKey(State, null = True, on_delete = models.SET_NULL)
    dueBy = models.DateTimeField()
    plannedStart = models.DateTimeField()
    startedAt = models.DateTimeField(null = True)
    completedAt = models.DateTimeField(null = True)
    createdBy = models.ForeignKey(User, related_name = 'subTaskCreatedBy', null = True, on_delete = models.SET_NULL)
    createdAt = models.DateTimeField(auto_now_add = True)
    modifiedBy = models.ForeignKey(User, related_name = 'subTaskModifiedBy', null = True, on_delete = models.SET_NULL)
    modifiedAt = models.DateTimeField(auto_now = True)

class TaskTag(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete = models.CASCADE )
    linkedBy = models.ForeignKey(User, null = True, on_delete = models.SET_NULL)

class TaskTeams(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    team = models.ForeignKey(Team, on_delete = models.CASCADE)

class TeamMembers(models.Model):
    team = models.ForeignKey(Team, on_delete = models.CASCADE)
    member = models.ForeignKey(User, on_delete = models.CASCADE)

class ActivityLog(models.Model):
    subtask = models.ForeignKey(SubTask, on_delete = models.CASCADE)
    starttime = models.DateTimeField(auto_now_add = True)
    endtime = models.DateTimeField(null = True)
    duration = models.FloatField(null = True)
    description = models.TextField(null = True)
    createdAt = models.DateTimeField(auto_now_add = True)
    createdBy = models.ForeignKey(User, related_name='activityLogCreatedBy', null = True, on_delete = models.SET_NULL)
    modifiedAt = models.DateTimeField(auto_now = True)
    modifiedBy = models.ForeignKey(User, related_name = 'activityLogModifiedBy', null = True, on_delete = models.SET_NULL)





