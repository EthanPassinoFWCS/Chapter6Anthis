favorite_places = {
  'Ethan': ["Fort Wayne", "Tampa", "Home"],
  'Hallie': ["Fort Wayne", "Japan", "Tennessee"],
  'Vince': ["Fort Wayne", "Tampa", "Tennessee"]
}

for person, places in favorite_places.items():
  print(f"{person}'s favorite places are: ")
  for place in places:
    print(place)
  