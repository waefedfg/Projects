import requests
import webbrowser
import json

game_id = input("Game ID:\n")


global smallest
smallest = None

def get_universe(game_id):
	url = f"https://apis.roblox.com/universes/v1/places/{game_id}/universe"
	response = requests.get(url)
	data = response.json()
	universeId = data.get("universeId")
	print(universeId)
	return universeId

def list_places(universeId):
	url = f"https://develop.roblox.com/v1/universes/{universeId}/places?limit=100"
	response = requests.get(url)
	places = response.json()['data']
	for idx, place in enumerate(places):
		print(f"{idx + 1}. {place['name']}")

	choice = input(f"Which place do you want to join?")
	choice = int(choice)

	the_choicer = places[choice - 1]
	print(the_choicer)
	print(the_choicer['name'])
	return the_choicer['id']


def smallest_server(universeId):
	url = f"https://games.roblox.com/v1/games/{universeId}/servers/Public"
	params = {
	"sortOrder": "Asc",
	"limit": 100
	}
	response = requests.get(url, params=params)
	servers = response.json()['data']
	if servers:
		smallest = servers[0]

		for i in servers:
			if i["playing"] < smallest["playing"]:
				smallest = i
		return smallest["id"]
	else:
		return None

universeId = get_universe(game_id)
place_choice = list_places(universeId)
game_instance = smallest_server(place_choice)

if game_instance:
	webbrowser.open(f"roblox://placeId={place_choice}&gameInstanceId={game_instance}")
else:
	webbrowser.open(f"roblox://placeId={place_choice}")