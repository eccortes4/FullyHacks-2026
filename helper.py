import json


def globalCoordToAnimalInfoDict(lat: float, long: float) -> str:
  fixed_coord_strs = ["32 -180", "40 -170", "42 -160", "33 -130"]

  with open('data.json', 'r') as file:
    data = json.load(file)


  if long < -178.75:
    return data[fixed_coord_strs[0]]
  elif long < -162.5:
    return data[fixed_coord_strs[1]]
  elif long < -146.25:
    return data[fixed_coord_strs[2]]
  else:
    return data[fixed_coord_strs[3]]


print(globalCoordToAnimalInfoDict(32, -180))
