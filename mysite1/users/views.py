from django.shortcuts import render
from django.shortcuts import redirect
from . import forms

# Create your views here.
def signup(request):
    if request.POST:
        form = forms.RegistrationFrom(request.POST)
        # username = form.cleaned_data.get('username')
        if form.is_valid():
            form.save()
            return redirect('signup')
    form = forms.RegistrationFrom()

    return render(request,'users/signup.html',{'form':form})
