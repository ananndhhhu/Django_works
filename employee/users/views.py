from django.shortcuts import render,redirect

from django.views import View


from users.forms import AddnewForm
from users.models import Employee
# Create your views here.
from django.views import View
# Create your views here.

def Home(request):
    return render(request,'home.html')


class AddNew(View):
    def get(self,request):
        form_instance = AddnewForm()
        context = {'form': form_instance}
        return render(request, 'addnew.html', context)

    def post(self,request):
        form_instance = AddnewForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('users:list')

class List(View):
    def get(self,request):
        E= Employee.objects.all()
        context = {'users':E}
        return render(request,'list.html',context)

class Detail(View):
    def get(self,request,i):
        E = Employee.objects.get(id=i)
        context = {'users': E}
        return render(request, 'detail.html', context)


class Edit(View):
    def get(self, request,i):
        m = Employee.objects.get(id=i)
        form_instance = AddnewForm(instance=m)
        context = {'form': form_instance}
        return render(request, 'edit.html', context)

    def post(self,request,i):
        m = Employee.objects.get(id=i)
        form_instance = AddnewForm(request.POST,request.FILES,instance=m)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('users:list')

class Delete(View):
    def get(self,request,i):
        m = Employee.objects.get(id=i)
        m.delete()
        return redirect('users:list')

