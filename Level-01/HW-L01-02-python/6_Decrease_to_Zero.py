# program to compute steps of the number to decrease to zero 
# if the number is even, then the number division by 2
# if the number is odd, then the number minus one

number = int(input())
counter = 0

while(number):
    if number % 2 == 0:
        number /=  2
    else:
        number -= 1
    counter += 1

print(counter)