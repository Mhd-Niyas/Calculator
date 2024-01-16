from django.shortcuts import render

# Create your views here.

def Calculator(req):
    return render(req,"Calculator.html")