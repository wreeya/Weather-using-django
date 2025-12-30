from django.shortcuts import render
from django.contrib import messages
import requests
import datetime
import os

# Create your views here.
def home(request):
     if 'city' in request.POST:
          city = request.POST['city']
     else:
          city = 'kathmandu'

     url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("OPENWEATHER_API_KEY")}'
     params = {'units': 'metric'}
     API_key = os.getenv('GOOGLE_API_KEY')
     SEARCH_ENGINE_ID = os.getenv('SEARCH_ENGINE_ID')

     query = city + "1920*1080"
     page = 1
     start = (page - 1) * 10
     searchType= 'image'
     city_url = f"https://www.googleapis.com/customsearch/v1?key={API_key}&cx={SEARCH_ENGINE_ID}&q={query}"

     data = requests.get(city_url).json()
     count = 1
     search_items = data.get("items")
     image_url = search_items[1]['link']

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
                            'city':city,
                    'exception_occured':False,
                    'image_url':image_url})
     except:
        exception_occured=True
        messages.error(request,'entered data is not available to API')
        day=datetime.date.today()

        return render(request, 'weatherapp/index.html',
                      {'description': 'clear sky',
                       'icon': 'Old',
                       'temp': 25,
                       'day': day,
                       'city': 'kathmandu',
                       'exception_occured': True,
                       'image_url': 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'})
