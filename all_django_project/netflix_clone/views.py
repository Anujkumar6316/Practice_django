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


def browse(request):
    return render(request, 'netflix_clone/user_dashboard/browse.html')

def tvshow(request):
    return render(request, 'netflix_clone/user_dashboard/tvshow.html')

def movies(request):
    return render(request, 'netflix_clone/user_dashboard/movies.html')

def latest(request):
    return render(request, 'netflix_clone/user_dashboard/latest.html')

def mylist(request):
    return render(request, 'netflix_clone/user_dashboard/mylist.html')

def search(request):
    return render(request, 'netflix_clone/user_dashboard/search.html')

def home(request):
    return render(request, 'netflix_clone/user_dashboard/user-profile/home.html')

def logout_page(request):
    return render(request, 'netflix_clone/logout.html')

def single(request):
    return render(request, 'netflix_clone/user_dashboard/single.html')