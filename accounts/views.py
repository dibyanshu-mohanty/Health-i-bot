from django.shortcuts import render ,redirect
from django.contrib import messages , auth
from django.contrib.auth.models import User
import requests
# Create your views here.
def register(request):
    if request.method== "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        username=request.POST['username']
        password=request.POST['password']
        password2=request.POST['password2']
        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That Username is taken.')
                return redirect('index')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is being used.')
                    return redirect('index')
                else:
                    user=User.objects.create_user(username=username , password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request,"You are now registered and can Log In")
                    return redirect('index')
        else:
            messages.error(request,'Passwords Donot match')
            return redirect('index')
    else:
        return render(request, 'pages/index.html')

def login(request):
    if request.method == "POST":
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are now logged in.")
            return redirect('dashboard')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('index')
def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are now logged out")
        return redirect('index')

def dashboard(request):
    x=[]
    y=[]
    lst=[]
    tst=[]
    d_list=[]
    t_list=[]
    response =  requests.get('https://api.thingspeak.com/channels/1382546/feeds.json?results=2').json()
    data = response['feeds']
    for i in range(2):
        lst=data[i]['created_at'][:10]
        tst=data[i]['created_at'][11:19]
        d_list.append(lst)
        t_list.append(tst)
        x.append(data[i]['field1'])
        y.append(data[i]['field2'])
    tdata=data[1]['field2']
    hdata=data[1]['field1']
    print(x)
    context = {
        'data': data,
        'lst':lst,
        'tst':tst,
        'tdata':tdata,
        'hdata':hdata
    }
    return render(request, "accounts/dashboard.html",context)