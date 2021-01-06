from django.db import models
class Exam(models,Model):
Question=models.CharField(max.length=100)
Option1=models.CharField(max.length=100)
Option2=models.CharField(max.length=100)
Option3=models.CharField(max.length=100)
Option4=models.CharField(max.length=100)
Corrans=models.CharField(max.length=100)
class Meta:
    db_table="onlineexam"