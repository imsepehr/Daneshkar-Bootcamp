# get a string as an input and check if it palindrome or not

my_string = input("Please enter your string: ")

my_string = my_string.upper() # upper case string
reverse_string = my_string [::-1] # reverse string

if reverse_string == my_string:
    print("Yes") # if input string is palindrome then print "Yes"
else:
    print("No") # if input string is not palindrome then print "No"
