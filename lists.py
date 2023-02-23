# list
list_one = ['D','r','.'," ", 'D','r','e']

# print 'D','r','e'
print(list_one[4:7])

# print all the items in the list
print(list_one[:])

# delete items from the first item to the 4th item
del list_one[0:4]

print(list_one[:])

countries = ['Kenya', 'Ghana', 'Ethiopia']
print(countries[1])

# updating countries list
countries[2]= 'Nigeria'
countries.append('Cameroon')

print(countries[:])
