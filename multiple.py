""" Weather report printing output in a pdf file format"""
import requests  # importing requests for extracting the data using url it makes simple
from datetime import datetime  # importing date and time
import pytz  # importing pytz for taking certain country timezone
from pds import pdf_file
# API key and url
apikey1 = "5b420cc97b3e8854d34ef3f969298896"
base_url1 = "https://api.openweathermap.org/data/2.5/weather?q="

apikey2 = "26042f968b6e4a4b907cb321bfbcd425"
base_url2 = "https://api.weatherbit.io/v2.0/current?lat=35.7796&lon=-78.6382&key="

while True:
    try:
        city1 = input("please entre the city name:- ")  # taking city as user choice
        # full url and getting json format for given city
        full_url = base_url1 + city1 + "&appid=" + apikey1
        data1 = requests.get(full_url).json()

        full_url2 = base_url2 + apikey2 + "city=" + city1
        data2 = requests.get(full_url2).json()

        timeZ_Kl = pytz.timezone('Asia/kolkata')  # time and date
        dt_Kl = datetime.now(timeZ_Kl)

        # fetching info from the json format using keys
        temp_max1 = int(data1['main']['temp'] - 273.15)
        weather_city1 = (data1['weather'][0]['main'])
        wind1 = (data2['data'][0]['wind_spd'])
        humidity1 = (data1['main']['humidity'])
        with open(f"vahini.txt", mode="a") as file:  #
            file.write("\n" + f'{dt_Kl.strftime("                                             date:-%d-%m-%y")}  \n{dt_Kl.strftime("                                             Time:- %H:%M:%S")}  \nCity:- {city1}')
            file.write("\n" + f"weather looking like- {weather_city1} \nmaximum temperature- {temp_max1}°C \nwind speed- {wind1} \nhumidity- {humidity1} \n")
            file.write("--------------------------------------------------------------------")
        ask = input("Do you want weather info for another city[say yes/no]?: ")  # taking user choice to weather used want info of another city or not
        while True:
            if ask in ['yes', 'y', 'yes i want to continue', 'YES']:
                print("Ok")
                break
            elif ask in ['no', 'n', 'no i dont want to continue', 'NO']:
                pdf_file()
                break
            else:
                print("Sorry I am not understood")
                break
    #  rectification of all errors
    # except KeyError:
    #     print("City not found")
    except requests.exceptions.SSLError:
        print("Please make sure you are connected to internet or not")


