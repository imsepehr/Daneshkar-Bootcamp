def power(n:int,m:int) -> (int):
    """ function to compute the power of number

    Args:
        n (int): base number
        m (int): power number

    Returns:
        int: return result n(base) power of m(power) """
      
    return n ** m


def is_happy(number : int) -> (bool):
    """
    function to check if number is happy or not 

    Args:
        number (int): number to check happy or not

    Returns:
        bool: if number is happy return True if number is not return False
    """    
    for i in range(0,200): #for prevent infinite loop
        sum = 0
        for digits in str(number):
            sum += power(int(digits),2)
        if sum == 1:
            return True
        number = sum
        
    return False


number = int(input())
print(is_happy(number))