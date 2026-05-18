from django.shortcuts import render, redirect
from books.forms import AddbooksForm
from books.models import Book
# Create your views here.
from django.views import View
def home(request):
    # context={'name':"Arun",'age':23}
    return render(request,'home.html')
#
# def add(request):
#     if(request.method=='POST'):
#         form_instance=AddbooksForm(request.POST)
#         if form_instance.is_valid():
#             # data = form_instance.cleaned_data
#             # t=data['title']
#             # a=data['author']
#             # p=data['price']
#             # pg=data['pages']
#             # l=data['language']
#             #
#             # print(t,a,p,pg,l)
#             #
#             #
#             # b=Book.objects.create(title=t,author=a,price=p,pages=pg,languages=l)
#             # b.save()
#
#             form_instance.save()
#
#             return render(request,'addbook.html')
#
#     if (request.method == 'GET'):
#         form_instance = AddbooksForm()
#
#         context = {'form': form_instance}
#
#         return render(request, 'addbook.html', context)
#
#
#
#
# def list(request):
#     if (request.method == 'GET'):
#         b=Book.objects.all()
#         context={'books':b}
#         return render(request,'booklist.html',context)




class AddBook(View):

    def get(self,request):
        form_instance = AddbooksForm()
        context = {'form': form_instance}
        return render(request, 'addbook.html', context)

    def post(self,request):
        form_instance = AddbooksForm(request.POST, request.FILES)
        if form_instance.is_valid():
            form_instance.save()
        return redirect('books:list')

class List(View):
    def get(self,request):
        b=Book.objects.all()
        context={'books':b}
        return render(request,'booklist.html',context)


class DetailView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        context={'book':b}
        return render(request,'detail.html',context)

class DeleteView(View):
    def get(self,request,i):
        b=Book.objects.get(id=i)
        b.delete()
        return redirect('books:list')


class EditView(View):
    def post(self,request,i):
        b=Book.objects.get(id=i)
        form_instance=AddbooksForm(request.POST,request.FILES,instance=b)
        if form_instance.is_valid():
            form_instance.save()
            return redirect('books:list')
    def get(self,request,i):
        b = Book.objects.get(id=i)
        form_instance=AddbooksForm(instance=b)
        context={'form':form_instance}
        return render(request,'edit.html',context)


