from django.db import models

class student(models.Model):
    name=models.CharField(max_length=200)
    roll_no=models.IntegerField(unique=True)
    dob=models.DateField()

    def __str__(self):
        return self.name
class mark(models.Model):
    student=models.ForeignKey(student, on_delete=models.CASCADE,unique=True)
    mark=models.FloatField()
    def __str__(self):
        return self.student.name
# Create your models here.
