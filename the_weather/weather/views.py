from pdb import set_trace
from django.http.response import HttpResponse
import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def home(request):
    return render(request,'home.html')

def index(request):
    # url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=85f2fcac7930e6aeadbe015ddf092460"

    url="http://api.openweathermap.org/data/2.5/weather?q={}&appid=85f2fcac7930e6aeadbe015ddf092460"


    weather_data = []
    if request.method=='POST':
        city=request.POST.get('c')

    try:
        r = requests.get(url.format(city)).json()
        city_weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

    except:
        return HttpResponse('Try with correct Spell')

    weather_data.append(city_weather)

    context = {'weather_data' : weather_data}
    return render(request, 'weather/weather.html', context)

