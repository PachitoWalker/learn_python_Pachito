import requests
import json 

url = "https://swapi.dev/api/" # Сайт со звездными войнами
response = requests.get(url).json()

print(response)

people_api = response.get("people")
print(people_api)

def check_people(url):
    for i in range(1, 10): # Получить имена первых 10 людей
        response = requests.get(f"{url}/{i}").json()    #получить из ответа данные по ссылке url/i (например https://swapi.dev/api/people/1)
        print(response.get("name")) # из response получить name.

check_people(people_api)



def check_planet(url):
    for i in range(1, 10):
        response = requests.get(f"{url}/{i}").json()
        print(response.get('name'))

planet_api = response.get("planets")

check_planet(planet_api)


print(requests.get(planet_api).json())

def max_d(url):
    diametrs_list = []
    for i in range(1,61):
        response = requests.get(f"{url}/{i}").json()
        diam = response.get("dimeter")
        name = response.get("name")
        diametrs_list.append({name:diam})
    print(diametrs_list)

max_d(planet_api)