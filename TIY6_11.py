cities = {
  'Fort Wayne': ["USA", "267,633", "On of the cheapest cities to live in the US."],
   "Miami": ["USA", "470,914", "the only US city that was founded by a woman."], 
   "LA": ["USA", "3,990,000", "The highest number of Mexicans (apart from Mexico) lives here."]}

for city, info in cities.items():
  print(city)
  print("Country: " + info[0])
  print("Population: " + info[1])
  print("Fun Fact: " + info[2])

