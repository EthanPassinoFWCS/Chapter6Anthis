pet1 = {"animal": "dog", "owner": "Ethan"}
pet2 = {"animal": "cat", "owner": "James"}
pet3 = {"animal": "monkey", "owner": "Charles"}
pet4 = {"animal": "tiger", "owner": "Nick"}

pets = [pet1, pet2, pet3, pet4]

for pet in pets:
  for key, value in pet.items():
    print(f"{key}: {value}")
