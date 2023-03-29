from django.db import models
import random
import string

status_options =(
    ('0','Uncompleted'),
    ('1','Completed')
    )

class Tasks(models.Model):
    task = models.CharField(default="",max_length=600)
    status = models.CharField(max_length=1,choices=status_options,default="0")
    added_on = models.DateTimeField(auto_now_add=True,)
  
    class Meta:
        verbose_name_plural = "Tasks"
        ordering = ['-added_on']

    def __str__(self):
        return self.task