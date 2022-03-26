from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'home.html', {'name': 'Timz Owen'})


def addition(request):
    val1 = int(request.POST["num1"])
    val2 = int(request.POST["num2"])
    res = val2 + val1

    return render(request, 'result.html', {'result': res})
