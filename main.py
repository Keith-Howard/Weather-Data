import requests


def get_weather_request(api_key, user_input, geographic_data):
    if user_input == 1:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?q='
                                + geographic_data[0] + '&appid=' + api_key)
    elif user_input == 2:
        response = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='
                                + str(geographic_data[0]) + ',' + geographic_data[1] + '&appid=' + api_key)
    else:
        response = requests.get('http://api.openweathermap.org/data/2.5/find?lat=' +
                                str(geographic_data[0]) + '&lon=' + str(geographic_data[1]) +
                                '&cnt=' + str(geographic_data[2]) + '&appid=' + api_key)
    return response.json()


def get_weather_data(get_request):
    json_to_python_data = get_request
    if str(json_to_python_data["cod"]) == "200":  # cod return code might be an int or a string
        main_key = json_to_python_data["main"]
        current_temperature = main_key["temp"]
        current_pressure = main_key["pressure"]
        current_humidity = main_key["humidity"]
        weather_key = json_to_python_data["weather"]
        weather_description = weather_key[0]["description"]
        print(json_to_python_data)

        print(" City = " + json_to_python_data["name"] +
              "\n Temperature (fahrenheit) = " +
              str(kelvin_to_fahrenheit(current_temperature)) +
              "\n Atmospheric pressure (in hPa unit) = " +
              str(current_pressure) +
              "\n Humidity (in percentage) = " +
              str(current_humidity) +
              "\n Description = " +
              str(weather_description))
    else:
        print(json_to_python_data["message"])


def get_weather_for_circle_area(get_request):
    json_to_python_data = get_request
    if str(json_to_python_data["cod"]) == "200":  # cod return code might be an int or a string
        for index in json_to_python_data['list']:
            main_key = index["main"]
            current_temperature = main_key["temp"]
            current_pressure = main_key["pressure"]
            current_humidity = main_key["humidity"]
            weather_key = index["weather"]
            weather_description = weather_key[0]["description"]

            print(' City = ' + index["name"] +
                  "\n Temperature (fahrenheit) = " +
                  str(kelvin_to_fahrenheit(current_temperature)) +
                  "\n Atmospheric pressure (in hPa unit) = " +
                  str(current_pressure) +
                  "\n Humidity (in percentage) = " +
                  str(current_humidity) +
                  "\n Description = " +
                  str(weather_description))
    else:
        print(json_to_python_data["message"])


def kelvin_to_fahrenheit(kelvin):
    return round(((kelvin - 273.15) * 9) / 5 + 32)


request_data = []
user_choice = int(input('Enter 1 for a single city, 2 for city via Zip Code and Country or 3 for an area of cities. '))
api_key = input('Enter Api Key. ')

if user_choice == 1:
    request_data.append(input('Enter city name. '))
    get_weather_data(get_weather_request(api_key, user_choice, request_data))
elif user_choice == 2:
    request_data.append(input('Enter Zip Code. '))
    request_data.append(input('Enter 2 letter Country Code, '))
    get_weather_data(get_weather_request(api_key, user_choice, request_data))
else:
    request_data.append(input('Enter latitude. '))
    request_data.append(input('Enter Longitude. '))
    request_data.append(input('Enter amount of Cities. '))
    get_weather_for_circle_area(get_weather_request(api_key, user_choice, request_data))
