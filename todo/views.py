from django.shortcuts import render
from django.utils.html import strip_tags
from django.core import serializers
from .models import Tasks
from django.http import *
import json

# Create your views here.
def home(request):
   return render(request,'home.html')

def add_task(request):
    if request.method == "POST":
       if len(request.POST['atask']) < 5:
               return JsonResponse({"error":True,"message":"Task should atleast be 5 letters long"},safe=False)
               
       inp = strip_tags((request.POST['atask']))
       try:
         tasks = Tasks.objects.filter(task=inp)
         if tasks.exists():
            return JsonResponse({"error": True, "message": "Task already exists"})
         else:
           tsk_model =Tasks(task=inp)
           tsk_model.save()
           return JsonResponse({"error":False,"message":"Added Successfully."},safe=False)

       except Exception as e:
                  return JsonResponse(json.dumps({"error":True,"message":e}),safe=False)

       return render(request,'home.html')
    return HttpResponseNotFound()

def list_tasks(request):
   if request.method == "POST":
      tsk_model = serializers.serialize('python', Tasks.objects.all(), fields=('task', 'status'))
      for d in tsk_model:
         del d['model']
      return JsonResponse(tsk_model,safe=False)
   return HttpResponseNotFound()
   
def delete_task(request):
   if request.method == 'POST':
      id = request.POST.get('id')
      if Tasks.objects.filter(pk=id).exists() is False:
         return JsonResponse({"error":True,"message":"Task Doesn't exists."},safe=False)
      else:
         try:
            task = Tasks.objects.get(pk=id)
            task.delete()
            return JsonResponse({"error":False,"message":"Task Deleted."},safe=False)
         except Exception as e:
            return JsonResponse({"error":True,"message":"Error occured while deleting the task."},safe=False)

   else:
      return HttpResponseNotFound()

def change_task_status(request):
   if request.method == "POST":
     id = request.POST['id']
     if Tasks.objects.get(pk=id) == False:
         return JsonResponse({"error":True,"id":id,"status":"Task Doesn't exists"},safe=False)
     else:
       default_task_status = Tasks.objects.get(pk=id).status
       if default_task_status == "0":
         task_model = Tasks.objects.get(pk=id)
         task_model.status = 1
         task_model.save()   
       else:
         task_model = Tasks.objects.get(pk=id)
         task_model.status = 0
         task_model.save()   
       return JsonResponse({"error":False,"id":id,"status":Tasks.objects.get(pk=id).status},safe=False)
      

   return HttpResponseNotFound()
   