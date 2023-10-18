from django.shortcuts import render

# Create your views here.

#función para ver la página home 

def home(request):
    return render(request, 'home/home.html')

