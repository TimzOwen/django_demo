from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Timz Owen'})


# function to do the addition operations
def add(request):
    val1 = int(request.GET['num1'])
    val2 = int(request.GET['num2'])
    result = val2 + val1

    return render(request, 'results.html', {'results': result})
