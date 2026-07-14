numbers = [-1, -3, -5, 0, 2, 4, 8, 17, -104]
# list of numbers
counter_positive = 0
sum_positive = 0

#loop for determining the number of positive numbers and their sum.
for num in numbers:
    if num > 0:
        counter_positive +=1
        sum_positive += num

#prints the requested information
print("Number list: ", numbers)
print("Number of positives: ", counter_positive)
print("Sum of positives: ", sum_positive)
