from django.shortcuts import render

# Create your views here.

def app03_index(request):
    return render(request, 'app03/index.html')