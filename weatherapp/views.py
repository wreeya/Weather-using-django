from django.shortcuts import render
import requests
import datetime
# Create your views here.
def home(request):
     if 'city' in request.POST:
          city = request.POST['city']
     else:
          city = 'kathmandu'

     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=a219d17523ea8a1fcb23e6c3d101a93a'
     params = {'units': 'metric'}

     try:

        data = requests.get(url, params=params).json()   # <-- FIX here: use params=params

        description = data['weather'][0]['description']
        icon = data['weather'][0]['icon']
        temp = data['main']['temp']

        day = datetime.date.today()

        return render(request, 'weatherapp/index.html',
                   {'description':description,
                            'icon':icon,
                            'temp':temp,
                            'day':day,
                            'city':city})
     except:
