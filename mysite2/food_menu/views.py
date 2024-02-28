from django.shortcuts import render, redirect
from .models import Food
from .forms import FoodForm

# Create your views here.
def index(request):
    Item_list = Food.objects.all()
    return render(request,'food_menu/index.html',{"Item_list":Item_list})

def add_item(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodForm()
    return render(request,'food_menu/add_items.html',{"form":form})

def details(request,id):
    item = Food.objects.get(id=id)
    return render(request,'food_menu/details.html',{"item":item})

def edit_item(request,id):
    item = Food.objects.get(id=id)
    print(item)
    if request.method == "POST":
        form = FoodForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = FoodForm(instance=item)
    print(form)
    return render(request, 'food_menu/edit_item.html', {"form":form})