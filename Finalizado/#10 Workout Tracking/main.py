import requests
import datetime


##### Personal Values #####
gender = "male"
weight_kg = 70
height_cm = 1.74
age = 21

APP_KEY = "4f2e014f341d10a6cf0b408ec309499c"
APP_ID = "0cc7432c"

today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

##### API Nutrition Settings #####
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_input = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY
}

parameters = {
    "query": exercise_input,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

nutrition_response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = nutrition_response.json()

print(result)

##### Sheety Settings #####
Google_Spreadsheets = "https://docs.google.com/spreadsheets/d/1Cvr-YdWjO2Z3byCrm9VO6XdliX6YrGK9NPekhlEHCek/edit#gid=0"
sheety_endpoint = "https://api.sheety.co/dc5d2239a16439a4caf16fe0dcabc3d5/myWorkouts/workouts"
sheety_headers = {"Authorization": "Bearer Oaishd&5kANu58!"}

for exercise in result["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_response = requests.post(url=sheety_endpoint, json=sheety_inputs, headers=sheety_headers)

print(sheety_response.text)
