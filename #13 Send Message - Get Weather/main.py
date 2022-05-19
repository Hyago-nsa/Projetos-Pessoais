import os
import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


telefone = ["+5522992269294", "+5522998575798", "+5521981918730", "+5522981813045"]
nome = ["Hyago", "Ana", "Leticia", "Amanda"]
lat_y = [-22.8636192, -22.8636192, -22.906847, -22.878679]
lon_x = [-42.3336313, -42.3336313, -43.172897, -42.019878]

TWILLIO_PHONE = "+16503380654"
TWILLIO_TOKEN = "47886473a5c693fa233c98fee3a71464"
TWILLIO_SID = "ACe71cde507364e216056eabf53275f32f"

API_KEY_OWM = "1d024efacc1aabb02616eb64ae5f9b2f"
ENDPOINT_OWN = "https://api.openweathermap.org/data/2.5/onecall"


for n in range(len(telefone)):
    weather_params = {
        "lat": lat_y[n],
        "lon": lon_x[n],
        "appid": API_KEY_OWM,
        "exclude": "current,minutely,daily"
    }

    response = requests.get(ENDPOINT_OWN, params=weather_params)
    response.raise_for_status()
    weather_data = response.json()
    weather_slice = weather_data["hourly"][:16]
    will_rain = False

    for hour_date in weather_slice:
        if int(hour_date["weather"][0]["id"]) < 800:
            will_rain = True

    if will_rain is True:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(TWILLIO_SID, TWILLIO_TOKEN, http_client=proxy_client)

        message = client.messages \
            .create(
            body=f"\nBom dia, {nome[n]}! 🌧\n"
                 f"Hoje vai chover... Eventualmente.\n"
                 f"Não esqueça de levar um guarda chuva! ☔",
            from_=TWILLIO_PHONE,
            to=telefone[n]
        )
        print(message.status)
        will_rain = False

    else:
        proxy_client = TwilioHttpClient()
        proxy_client.session.proxies = {'https': os.environ['https_proxy']}

        client = Client(TWILLIO_SID, TWILLIO_TOKEN)

        message = client.messages \
            .create(
            body=f"\nBom dia, {nome[n]}! 🌞\n"
                 f"Hooray! Hoje não vai chover.\n"
                 f"Psiu...Não esqueça de se hidratar! 🥤",
            from_=TWILLIO_PHONE,
            to=telefone[n]
        )
        print(message.status)

