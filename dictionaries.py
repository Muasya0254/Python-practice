capitals = {
  "Kenya": "Nairobi",
  "Ghana": "Accra",
  "Ethiopia": "Addis Ababa",
  "Zimbabwe": "Harare",
}

print(capitals["Kenya"])

statistics = {
    "count_how_many_at_least_ten": 0,
    "count_how_many_less_than_ten": 0,
}

data = [5, 9, 11, 4, 18]
for element in data:
    if element >= 10:
        statistics['count_how_many_at_least_ten'] += 1
    else:
        statistics['count_how_many_less_than_ten'] += 1

print(statistics["count_how_many_at_least_ten"])
print(statistics["count_how_many_less_than_ten"])

country_data = {
  "Kenya": {"capital": "Nairobi", "currency": "shilling"},
  "Ghana": {"capital": "Accra", "currency": "cedi"},
  "Ethiopia": {"capital": "Addis Ababa", "currency": "birr"},
}

print(country_data["Ghana"]["currency"])

def show_currencies():
    for country_name in country_data:
        # each time through the loop, we'll get a different country_name.
        all_country_data = country_data[country_name]
        print(all_country_data['currency'])

show_currencies()