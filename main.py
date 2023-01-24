import requests


cityName = input("Mettre le nom de la ville :")
langage = "fr"
clef = "3412f3d259dfcc04ad3293ac4784e2c8"

apiLien = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={clef}&lang={langage}&units=metric"

json = requests.get(apiLien).json()
temps = json['weather'][0]['description']
temperature = json["main"]

print(temperature['temp']) #Dans l'objet "main", le fait de mettre entre crochet le nom de la variable va la rechercher dans celui-ci
print(json)
print("    ")
print(f" Le temps à {cityName} est {temps}, il fait {temperature['temp']} degrés")