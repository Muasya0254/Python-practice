all_country_data = {
  "Kenya": {
        "capital": "Nairobi",
        "currency": "shilling",
        "parks": [
          {
            "park_name": "Aberdare National Park",
            "size_km": 767
          },
          {
            "park_name": "Meru National Park",
            "size_km": 870
          }
        ]
    },
  "Ghana": {
        "capital": "Accra",
        "currency": "cedi",
        "parks": [
          {
            "park_name": "Mole National Park",
            "size_km": 4840
          },
          {
            "park_name": "Kakum National Park",
            "size_km": 375
          }
        ]
    },
}

# write a function that uses the data above
# to get a list of park names

def get_park_name(country_name):
    results = []

    if country_name in all_country_data:
        country_data = all_country_data[country_name]
        parks = country_data["parks"]
        for park in parks:
            results.append(park["park_name"])
    else:
        print("could not find this country")

    return results

country = input("Enter country: ")
print(get_park_name(country))