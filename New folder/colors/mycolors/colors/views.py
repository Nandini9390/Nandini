from django.shortcuts import render
from django.http import HttpResponse
def red(request):
    return render(request, 'red.html')

def pink(request):
    return render(request, 'pink.html')


def orange(request):
    return render(request, 'orange.html')