# get 3 number then return maximum of them 
 
number_1 = float(input())
number_2 = float(input())
number_3 = float(input())

max = number_1

if number_2 >= max:
    max = number_2
if number_3 >= max:
    max = number_3

print(max)

def test_git(x):
    print(x)