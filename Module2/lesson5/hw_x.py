import requests

url = "https://swapi.dev/api/starships"

response = requests.get(url).json()

all_starships = response.get("results")
speeds = []
count = 0
for starship in all_starships:
    speed = starship.get("max_atmosphering_speed")
    if count < 5 and speed !='n/a' and speed.isdigit(): #isdigit - помогает удалить все не числовые значения
        speeds.append(int(speed))
        count += 1

print(speeds)
print(max(speeds))

