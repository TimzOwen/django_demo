from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Timz Owen'})


def addition(request):
    val1 = int(request.GET["num1"])
    val2 = int(request.GET["num2"])
    res = val2 + val1

    return render(request, 'results.html', {'result': res})
