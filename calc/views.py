from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Timz Owen'})


# function to do the addition operations
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    result = val2 + val1
    return render(request, 'results.html', {'results': result})


def division(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    results = val1 / val2
    return render(request, 'results.html', {'res': results})
