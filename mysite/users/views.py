from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import Register_user

# Create your views here.
def login(request):
    return render(request,'users/login.html')

def register_user(request):
    if request.method == "POST":
        form = Register_user(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'users/login.html')
    else:
        form = Register_user()
    return render(request,'users/register_user.html',{'form':form})