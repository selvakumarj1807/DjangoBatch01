from django.shortcuts import render

# Create your views here.

def app01_index(request):
    return render(request, 'app01/index.html')