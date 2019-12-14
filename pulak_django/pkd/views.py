from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html', {'mail': 'xyz@abc.com'})


def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val1 + val2
    return render(request, 'result.html', {'result': result})


def subtract(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val1 - val2
    return render(request, 'result.html', {'result': result})


def back(request):
    return render(request, 'home.html')
