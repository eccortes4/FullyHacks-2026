import json

from location_animal_data import getCoordsToAnimalDataDict

fixed_quadrant_coords = [
  (32, -180),
  (40, -170),
  (42, -160),
  (33, -130),
  (20, -192),
  (16, -175),
  (25, -150),
  (21, -145),
  (8,  -180),
  (1,  -163),
  (11, -159),
  (15, -146)
]

data = getCoordsToAnimalDataDict(fixed_quadrant_coords, 3)

print(data)

#with open("data.json", "w") as data_file:
#  json.dump(data, data_file)
