from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact
# Create your views here.
def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        contact= Contact(name=name,email=email,phone=phone,message=message)

        contact.save()
        
        send_mail(
            'Inquiry on Health-i-Box',
            message,
            'biz.binary404@gmail.com',
            ['dibyanshu2002@gmail.com','preetish.biswal2020@vitstudent.ac.in'],
            fail_silently= False,
        )
        messages.success(request,"We will contact you soon.")
        return redirect('index')



