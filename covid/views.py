from django.shortcuts import render
import requests
# Create your views here.
def covids(request):
    url="https://api.rootnet.in/covid19-in/stats/latest"
    covid_list = []
    response=requests.get(url).json()
    r=response["data"]["regional"]
    context = {
        'r':r,
    }
    return render(request , 'covid/tracker.html',context)