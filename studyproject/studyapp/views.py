from django.shortcuts import render
from django.http import HttpResponse
from.models import place
from.models import team


def home(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,"index.html",{'result':obj,
                                        'results':obj1
                                        })



#def arithmetic_operations(request):
    #x = int(request.GET['num1'])
    #y = int(request.GET['num2'])

    #addition_result = x + y
   # multiplication_result = x * y

   # if y != 0:
        #division_result = x / y
    #else:
        #division_result = "Error: Division by zero"

   # subtraction_result = x - y

    #return render(request, "results.html", {'addition_result': addition_result,
                                            #'multiplication_result': multiplication_result,
                                            #'division_result': division_result,
                                            #'subtraction_result': subtraction_result})

