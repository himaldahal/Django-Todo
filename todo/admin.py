from django.contrib import admin
from .models import Tasks

# Register your models here.
@admin.register(Tasks)
class TasksAdmin(admin.ModelAdmin):
    list_display = ("task", "status","added_on")