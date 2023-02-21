from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,DetailView
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def index(request):
    return render(request,'index.html')
class tasklist(ListView):

    model = Task
    context_object_name = 'items'
    template_name = 'task.html'

class create(CreateView):
     
     model = Task
     fields = '__all__'
     success_url = reverse_lazy('items')
     template_name = 'create.html'

class Update(UpdateView):
     
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('items')
    template_name = 'create.html'
      
class Delete(DeleteView):
     
    model = Task
    context_object_name = 'items'
    success_url = reverse_lazy('items')
    template_name = 'delete.html'

class view(DetailView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('items')
    template_name = 'detail.html'

def signup(request):

    if request.method =='POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        myuser = User.objects.create_user(username,email,pass1)

        myuser.save()
        

        
        return redirect('signin')
    

    return render(request,'signup.html')
    

def signin(request):
    if request.method=='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request,user)
            fname = user.username
            return render(request,'task.html',{'fname': fname})

        else:
            return redirect('signin')

    return render(request,'signin.html')

def signout(request):
    logout(request)
    return redirect('signin')

