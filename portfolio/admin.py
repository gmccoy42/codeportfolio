from django.contrib import admin
from portfolio.models import projects

class ProjectsAdmin(admin.ModelAdmin):
    pass
admin.site.register(projects, ProjectsAdmin)