from django.shortcuts import render
from rest_framework import mixins, generics
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from student_api.serializers import Studentreg, AddMark
from .models import *


class student(mixins.ListModelMixin,
              mixins.CreateModelMixin,
              generics.GenericAPIView):
    serializer_class = Studentreg
    queryset = student.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class student_mark(mixins.ListModelMixin,
                   mixins.CreateModelMixin,
                   generics.GenericAPIView):
    serializer_class = AddMark
    queryset = mark.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class result(APIView):
    a = mark.objects.all()
    content = {}

    def get(self, request, *args, **kwargs):
        m = self.a
        content = {}
        count = 0
        a = 0
        b = 0
        c = 0
        d = 0
        e = 0
        f = 0
        for i in m:
            name = i.student.name
            mark = i.mark
            if mark > 90:
                a += 1
            elif mark > 80:
                b += 1
            elif mark > 70:
                c += 1
            elif mark > 60:
                d += 1
            elif mark > 55:
                e += 1
            elif mark < 55:
                f += 1
            count += 1
        dist=100*(a/count)
        f_class=100*((b+c)/count)
        passed=100*((count-f)/count)

        content["Total NO Of Student"] = count
        content["A"] = a
        content["B"] = b
        content["C"] = c
        content["D"] = d
        content["E"] = e
        content["f"] = f
        content["Distinction %"]=dist
        content["First class %"]=f_class
        content["Pass %"]=passed

        return Response(content)

# Create your views here.
