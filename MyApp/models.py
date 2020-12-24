from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=50)
    presence_num = models.IntegerField()
    grade = models.CharField(max_length=10)
    is_graduated = models.BooleanField()


    def __str__(self):
        return self.name

    

