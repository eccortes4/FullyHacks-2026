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
    size=50
  ).execute()

  scinames_names_depths = []

  for sci_name, name, depth in zip(data["scientificName"], data["vernacularName"], data["depth"]):
    if isinstance(name, str) and not math.isnan(depth):
      scinames_names_depths.append( (string.capwords(sci_name), string.capwords(name), depth) )

  #scinames_names_depths.sort(
  #  key=lambda sciname_name_depth : sciname_name_depth[2]
  #)

  return scinames_names_depths

# for testing
# 
# def printScinamesNamesDepth() -> None:
#   animalsData = getAnimalsAtLocation(lat=32, long=-170)

#   print("ANIMAL NAMES:")
#   for sci_name, name, depth in animalsData:
#     print(f"\t{name} ({sci_name})\t{depth}")

