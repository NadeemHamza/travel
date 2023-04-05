from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    team = Team.objects.all()
    # return HttpResponse("Hello World")
    # name = "Inmakes"
    return render(request, 'index.html', {'result': obj, 'team': team})

# def about(request):
#     return render(request, 'about.html')
#
#
# def contact(request):
#     return HttpResponse("Contact")
#
#
# def operation(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     add = x + y
#     sub = x - y
#     mul = x * y
#     div = x / y
#     return render(request, 'result.html', {'add': add, 'sub': sub, 'mul': mul, 'div': div})
