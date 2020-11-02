users = {
'aeinstein': {
'first': 'albert',
'last': 'einstein',
'location': 'princeton',
'birth': 'March 14, 1879',
'death': 'April 18, 1955'
},
'mcurie': {
  'first': 'marie',
  'last': 'curie',
  'location': 'paris',
  'birth': 'November 7, 1867',
  'death': 'July 4, 1934'
  },
}
for username, user_info in users.items():
  print(username)
  for key, value in user_info.items():
    print(f"{key}: {value}")
  