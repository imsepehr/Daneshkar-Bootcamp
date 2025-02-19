def convert_to_normalized(n:list[int]) -> (list):
    """ convert all elements in list to normalized

    Args:
        n (list): list of numbers to convert
    Returns:
        list: list of normalized numbers 
    """     
    new_list = []
    for i in range(len(n)):
        z = (n[i] - min(n)) / (max(n) - min(n))
        if z.is_integer():
            new_list.append(int(z))
        else:
            new_list.append(round(z, 3))

    return new_list


my_list = input().split()
for i in range(len(my_list)):
    my_list[i] = int(my_list[i])

print(convert_to_normalized(my_list))