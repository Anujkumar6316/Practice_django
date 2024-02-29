from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'netflix_clone/index.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('netflix_clone:login')
    else:
        form = UserCreationForm()
    return render(request, 'netflix_clone/register.html', {'form': form})


def home(request):
    return render(request, 'netflix_clone/user_dashboard/browse.html')