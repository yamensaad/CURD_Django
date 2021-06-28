from django.db import models

# Create your models here.


class grade(models.Model):
    title = models.CharField(max_length=50)


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    Student_code = models.CharField(max_length=3)
    mobile = models.CharField(max_length=15)
    grade = models.ForeignKey(grade, on_delete=models.CASCADE)
