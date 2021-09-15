import requests

def desc_and_temp():
    api_key = '89fa2aca3a5a0ca8b688c8cac4c6417e'
    city = 'Orlando'
    url = "http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=imperial"

    request = requests.get(url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp_min = json.get('main').get('temp_min')
    temp_max = json.get('main').get('temp_max')
    return {
        'desc' : description,
        'min': temp_min,
        'max' :temp_max}

def main():
    weather = desc_and_temp()
    print('Todays forecast is', weather['desc'], "with a low of", weather['min'], "and a high of", weather['max'])

main()