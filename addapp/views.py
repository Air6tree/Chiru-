from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):
  return render(request,'base.html'),

def show(request):
  x= int(request.GET['t1'])
  y= int(request.GET['t2'])

  z= x + y 

  return HttpResponse(z);