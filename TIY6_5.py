rivers = {"nile": "egypt", "Mississippi River": "USA", "Amazon River": "South America"}

for river, place in rivers.items():
  print(f"{river.title()} runs through {place}.")

for river in rivers:
  print(river.title())

for place in rivers.values():
  print(place.title())