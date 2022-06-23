from contextlib import nullcontext
import requests
import datetime

from urllib import request
from django.shortcuts import render
num = 3+3+34


def index(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kathmandu'

    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=1bf779b770c0a107b0cce8a6eec0f09c'

    r = requests.get(url.format(city)).json()

    description = r['weather'][0]['description']

    icon = r['weather'][0]['icon']
    temp = r['main']['temp']
    date = datetime.date.today()
    context = {
        'city': city,
        "descp": description,
        'temp': temp,
        'icon': icon,
        'date': date
    }

    return render(request, "index.html", context)
