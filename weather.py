from twilio.rest import TwilioRestClient

import requests
email = []

email_file = open('emails.txt', 'r')

for line in email_file:

    email.append(line.strip())      # removing the new line between two emails

def send_message():
    client = TwilioRestClient()
    client.messages.create(from_='5512259960',to = '5512259960',body = 'Ahoy from Twilio!')


def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?id=1259229&units=metric&APPID=****'
    weather_request=requests.get(url)
    weather_json=weather_request.json()
    print(weather_json)
    discription = weather_json['weather'][0]['description']
    print(discription)
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']

    print(temp_min)
    print(temp_max)

    forecast = 'The weather today is '
    forecast += discription + ' with a high of '+str(int(temp_min))
    forecast +=  '  with a low of '+str(int(temp_max))
    print(forecast)
def main():


    get_weather_forecast()
    send_message()
main()