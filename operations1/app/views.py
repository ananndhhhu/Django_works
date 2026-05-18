from django.db.models.expressions import result
from django.shortcuts import render

# Create your views here.
def home(request):
    if (request.method=="GET"):

        # execute when a post request is arrived

     return render(request,'home.html')

def addition(request):
    if (request.method == "GET"):

        #execute when a post request is arrived

        return render(request,'addition.html')

    if (request.method == "POST"):

        print(request.POST)

        num1=int(request.POST['n1'])
        num2 =int(request.POST['n2'])

        s=num1+num2

        context={'result':s}

        return render(request, 'addition.html',context)

def bmi(request):
    if (request.method == "GET"):
        return render(request,'bmi.html')
    if (request.method == "POST"):
        print(request.POST)

        weight = float(request.POST['n1'])
        height = float(request.POST['n2'])

        b=weight/(height**2)
        context = {'bmi': b}
        return render(request, 'bmi.html',context)



def factorial(request):
    if (request.method == "GET"):
        return render(request,'factorial.html')
    if (request.method == "POST"):
        print(request.POST)

        num1 = int(request.POST['n1'])
        fact=1
        for i in range(1,num1+1):
            fact=fact*i

            result=fact


        context = {'fact': result}
        return render(request, 'factorial.html',context)



