from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.core import serializers
import json


def index(request):
    if request.method == 'GET':
        return render(request, 'employee/index.html')


def show_all(request):
    data = serializers.serialize("json", Employee.objects.all())
    print data
    return HttpResponse(data)


def show_emp_with_code(request):
    data = Employee.objects.filter(emp_code=request.GET['emp_code'])
    context = {}
    if data is None:
        context['error']='No such employee exist'
    else:
        context = serializers.serialize("json",data)
        print context
        return HttpResponse(context)


def show_emp_with_nthsalary(request):
    n = request.GET['n_value']
    m=int(n)-1
    data=(Employee.objects.order_by('-salary')[m:n])
    #emp_list=list(data)
    context = serializers.serialize("json",data)
    print context
    return HttpResponse(context)