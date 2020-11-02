alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

alien_0['xpos'] = 0
alien_0['ypos'] = 25

print(alien_0)

alien_0['xpos'] = 90

print(alien_0)

del alien_0['points']

print(alien_0)

for key, value in alien_0.items():
  print(f"Key: {key}")
  print(f"Value: {value}")

for name in alien_0.keys():
  print(name)

for vs in alien_0.values():
  print(vs)


