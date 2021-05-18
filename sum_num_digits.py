# Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits.
# Let's assume that all numbers in the input will be integer values.

def sum_digits(number):
    # empty string which will store the absolute values of number as a string
    string_sum = ""
    
    # convert "number" to a string and loop through each element
    for i in str(number):
        # for every element that isn't a hyphen, add it to string_sum
        if i != "-":
            string_sum += i
    # new variable to count the value of each string after converting it to an int
    count = 0
    # looping through each element in the string
    for i in string_sum:
        # adding each element to "count" after converting it to an integer
        count += int(i)
    return count
