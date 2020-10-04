#Juan Nevarez
#CIS245
#10/4/2020
import requests
import webbrowser
import json


api_key = "14bf29c16ef6ec7b767c48e0749c43e5" #my api key from openweathermap.org #source below
units = "imperial" #changes units from standard to imperial
url1 = "http://api.openweathermap.org/data/2.5/weather?" #URL to api
degree_sign = u"\N{DEGREE SIGN}" #string to the degrees symbol for the temperature source below


city_name = input(" City name : ") #input city name
complete_url = url1 + "appid=" + api_key + "&q=" + city_name + "&units=imperial"
response = requests.get(complete_url)



x = response.json()

# the lines below send a request to the api to pull information such as the temp, skies, low temp, high temp #source below
if x["cod"] != "404":
    y = x["main"]
    current_temperature = y["temp"]
    current_temp_low = y["temp_min"]
    current_temp_max = y["temp_max"]

    z = x["weather"]
    weather_description = z[0]["description"] #pulls description from api



    print(" Current Temp: " +
          str(current_temperature) + (degree_sign) + (" F") +

          "\n Lowest temp today:  " +
          str(current_temp_low) + (degree_sign) + (" F") +

          "\n High temp today:  " +
          str(current_temp_max) + (degree_sign) + (" F") +

          "\n Skies:" +
          str(weather_description))







else:
    print(" City not found, please try again ")
    webbrowser.open('https://weather.com/', new=2) #opens browser when city is not displayed #source below






 #sources
 #https://www.dataquest.io/blog/python-api-tutorial/
 #https://www.geeksforgeeks.org/python-add-one-string-to-another/
#https: // elearning.wsldp.com / python3 / python - open - web - browser /
#https://developer.mozilla.org/en-US/docs/Web/API/Response
#https://openweathermap.org/current#data
#https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/
#https://www.w3schools.com/python/python_for_loops.asp
#https://www.w3schools.com/python/python_datatypes.asp
#https://weather.com/
#https://www.kite.com/python/answers/how-to-print-the-degree-symbol-in-python