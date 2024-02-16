from django.shortcuts import render
from .models import Id_details

# Create your views here.
def index(request):
    if request.POST:
        uid = request.POST.get('uid')
        name = request.POST.get('name') 
        course = request.POST.get('course')
        father_name = request.POST.get('father_name')
        mother_name = request.POST.get('mother_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        address = request.POST.get('address')

        details = Id_details(uid=uid,name=name,course=course,father_name=father_name,mother_name=mother_name,contact=contact,email=email,address=address)
        details.save()
        return render(request,'pdf/accept.html')
    
    return render(request,'pdf/accept.html')

def card(request,id):
    details = Id_details.objects.get(pk=id)
    return render(request,'pdf/card.html',{'details':details})