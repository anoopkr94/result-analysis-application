from rest_framework import serializers
from .models import *



class Studentreg(serializers.ModelSerializer):


    class Meta:
        model=student
        fields=["name","roll_no","dob"]



class AddMark(serializers.ModelSerializer):
    class Meta:
        model = mark
        fields = ["student", "mark"]


