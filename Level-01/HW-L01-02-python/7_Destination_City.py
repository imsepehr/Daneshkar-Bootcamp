def find_destination_city(paths: list[str]) -> (str):
  """this function takes a list of paths and returns destination city

  Args:
      paths (list[str]): list of cities paths

  Returns:
      str: destination city  
  """      

  # create a set of all cities
  # we use set properties to determine which cities doenst exit path and also to not add two same cities in the set
  cities = set()
  for path in paths:
    cities.add(path[0])
    cities.add(path[1])

  # create set of all cities that have exit path
  outgoing_cities = set()
  for path in paths:
    outgoing_cities.add(path[0])

  # create set of all cities that are in cities set but not in outgoing_cities set(that means all cities that have not exit path)
  destination_city = cities - outgoing_cities

  return destination_city.pop()


paths = input().split()
x = int(len(paths) / 2)
y = 2
my_list=[]
sublist=[]
j = 0
for i in range(x):
    sublist.append(paths[j])
    sublist.append(paths[j+1])
    j += 2
    my_list.append(sublist)
    sublist=[]

print(find_destination_city(my_list))

