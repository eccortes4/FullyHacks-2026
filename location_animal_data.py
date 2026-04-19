import re
import wikipedia

from find_animals import getAnimalsAtLocation


# [HELPER FOR getLocationAnimalData]
def getPageImageUrl(page) -> str:
  image_url = None
  for img_url in reversed(page.images):
    url_extension = img_url[-3:]
    if url_extension == "jpg":
      image_url = img_url
      break

  return image_url


# [HELPER FOR getLocationAnimalData]
def getCleanSummary(raw_summary: str) -> str:
  clean_summary = ""

  raw_summary = re.sub(r"==.*?==", " ", raw_summary)

  for i in range(len(raw_summary)):
    ch = raw_summary[i]

    if ch == "\n" or ch == "\'":
      continue

    clean_summary += ch

  return clean_summary


# List of dictionaries, each representing an animal with its info.
# Dict structure:
#   { name: <name>, }
def getLocationAnimalData(*, lat: float, long: float, max: int=7) -> list[dict]:
  animals_data = []
  animals = getAnimalsAtLocation(lat=lat, long=long)

  counter = 0
  for scientific_name, name, depth in animals:
    if counter == 5: break

    try:
      page           = wikipedia.page(name)
      animal_img_url = getPageImageUrl(page)
      raw_summary    = wikipedia.summary(name, sentences=3)

      if animal_img_url is None: continue

      animal_info = {
        "name" : name,
        "scientific_name" : scientific_name,
        "image_url" : animal_img_url,
        "depth" : depth,
        "summary" : getCleanSummary(raw_summary)
      }
      animals_data.append(animal_info)
      print(animal_info, "\n\n")
      counter += 1
    except(wikipedia.exceptions.PageError):
      pass

  animals_data.sort(key=lambda animal_info : animal_info["depth"])
  return animals_data


def stringifyCoords(lat: float, long: float) -> str:
  return f"{lat} {long}"


# Coords should be in lat-long.
def getCoordsToAnimalDataDict(coords: list[tuple[float, float]]) -> dict:
  coord_to_animals_data = {}

  for lat, long in coords:
    coord_to_animals_data[stringifyCoords(lat, long)] = getAnimalsAtLocation(lat=lat, long=long)

  return coord_to_animals_data
