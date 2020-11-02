favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

people = ["Jacob", "James", "phil", "Kaleb", "sarah"]

for person in people:
  if person in favorite_languages: print(f"{person}, thank you for taking the poll.")
  else: print(f"Hello, {person} please take our poll!")