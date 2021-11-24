from django.shortcuts import render

# Create your views here.
def jinja1(request):
    return render(request,'h1.html')