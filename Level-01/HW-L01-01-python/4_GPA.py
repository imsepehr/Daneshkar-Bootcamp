# get grade of 5 lessons and compute average of them and convert average to format of GPA 
# if one of inputs is greater than 20 then print "Invalid Grade" and program halted

lesson_1 = float(input())
lesson_2 = float(input())
lesson_3 = float(input())
lesson_4 = float(input())
lesson_5 = float(input())

# check if one of the lesson is greater than 20
if lesson_1 > 20 or lesson_2 > 20 or lesson_3 > 20 or lesson_4 > 20 or lesson_5 > 20: 
    print("Invalid Grade")
    exit()

#compute average
sum = lesson_1 + lesson_2 + lesson_3 + lesson_4 + lesson_5
avg = sum / 5

# convert average to GPA
if avg >= 18 and avg <= 20:
    print("A")
elif avg >= 15 and avg <= 17.99:
    print("B")
elif avg >=12 and avg <= 14.99:
    print("C")
elif avg >= 0 and avg <= 11.99:
    print("F")