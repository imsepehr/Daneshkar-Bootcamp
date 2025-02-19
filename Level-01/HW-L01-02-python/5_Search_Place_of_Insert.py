def place_of_insert(number_list:list, target:int) -> (int):
    """function to search the index of the given number target in the nuber_list
    if the target is not in the list then return the index of the desired place of insert
    

    Args:
        number_list (list): list of numbers
        target (int): number target to search
    Retruns:
        int: index of target number in nuber_list or if the target is not in the list then return the index of the desired place of insert
    """    
    for i in range(len(number_list)):
        if number_list[i] == target:
            return i
        elif target > number_list[i] and target < number_list[i+1]:
            return i +1
        
my_list = input().split()
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

target = int(input())

print(place_of_insert(my_list, target))