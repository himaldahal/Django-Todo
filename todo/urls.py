from django.urls import path
from .views import home,add_task,list_tasks,change_task_status,delete_task
urlpatterns = [
    path('',home),

    # apis
    path('add/',add_task,name="add-task"),
    path('delete/',delete_task,name="delete-task"),
    path('list/',list_tasks,name="list-task"),
    path('status_update/',change_task_status,name="update-task-status")

]
