# this is a program that first input number of words that you want to input itself and theirs meaning 
# then input a string that want to translate 
# then check if any words of in string is in dictionary then replace them with meaning in dictionary else keep itself


my_dict = {} # dictionary to save meaning of words

n = int(input())

# save meaninig in format key and value in dictionary
for i in range(0,n):
    key = input()
    value = input()
    my_dict[key] = value

my_string = input().split() # input string taht want to translate

# check if word of string is in dictionary then replace it with meaning of the word in dictionary
for i in range(len(my_string)):
    if my_string[i] in my_dict:
        my_string[i] = my_dict[my_string[i]]

new_string = ' '.join(map(str,my_string)) # convert list to string
print(new_string)


        

