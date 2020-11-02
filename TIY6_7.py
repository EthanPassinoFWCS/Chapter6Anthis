person1 = {'first_name': "Ethan", 'last_name': "Passino", 'age': 17, 'city': "Fort Wayne"}

person2 = {'first_name': "Hallie", 'last_name': "Passino", 'age': 19, 'city': "Fort Wayne"}

person3 = {'first_name': "Vince", 'last_name': "Passino", 'age': 49, 'city': "Fort Wayne"}

people = [person1, person2, person3]

for person in people:
  for key, value in person.items():
    print(f"{key}: {value}")
  