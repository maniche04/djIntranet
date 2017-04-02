from django.contrib import admin
from tasks import models
# from guardian.admin import GuardedModelAdmin

# Register your models here.
admin.site.register(models.Task)
admin.site.register(models.SubTask)
admin.site.register(models.State)
admin.site.register(models.Tag)
admin.site.register(models.TaskTag)
admin.site.register(models.Team)
admin.site.register(models.TaskTeams)
admin.site.register(models.TeamMembers)
admin.site.register(models.ActivityLog)
admin.site.register(models.Project)