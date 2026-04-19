import math
import string

from pyobis import occurrences

# Makes octagon polygon (to mimic circle). [HELPER FOR getScinamesNamesDepth]
def getWKTPolygonStr(lat: float, long: float, radius: float) -> str:
  return (f"POLYGON(({long - 0.7*radius} {lat + radius}, {long + 0.7*radius} {lat + radius}, " +  #top side
          f"{long + radius} {lat + 0.7*radius}, {long + radius} {lat - 0.7*radius}, " +  # right side
          f"{long - 0.7*radius} {lat - radius}, {long + 0.7*radius} {lat - radius}, " +  # bottom side
          f"{long - radius} {lat + 0.7*radius}, {long - radius} {lat - 0.7*radius}, " +  # left side
          f"{long - 0.7*radius} {lat + radius}))")  # repeat of first coord to connect polygon


# Sorted by depth (in meters), least to greatest.
def getAnimalsAtLocation(*, lat: float, long: float, radius: float=10) -> list[tuple[str, str, float]]:
  data = occurrences.search(
    taxonid=2,
    geometry=getWKTPolygonStr(lat, long, radius),
    size=60
  ).execute()

  scinames_names_depths = []
  animals_added = set()

  for sci_name, name, depth in zip(data["scientificName"], data["vernacularName"], data["depth"]):
    if isinstance(name, str) and not math.isnan(depth) and not sci_name in animals_added:
      if sci_name.lower() == "phacellophora camtschatica":  # special case 1 (name was not listed)
        name = "Fried Egg Jellyfish"
      elif sci_name.lower() == "ranzania laevis":  # special case 2 (name was in Japanese)
        name = "Slender Sunfish"
      elif name.lower() == "na":
        continue

      scinames_names_depths.append( (string.capwords(sci_name), string.capwords(name), depth) )
      animals_added.add(sci_name)

  col_names = list(data.columns)
  col_names.sort()

  return scinames_names_depths


def printScinamesNamesDepth(lat: float, long: float) -> None:
  animalsData = getAnimalsAtLocation(lat=lat, long=long)

  print("ANIMAL NAMES:")
  for sci_name, name, depth in animalsData:
    print(f"\t{name} ({sci_name})\t{depth}")


# printScinamesNamesDepth(21, -145)
