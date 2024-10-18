#The purpose of this program is to take in an integer value 'n' from the user and determine if it is a co-balancing number. If 'n' is a co-balancing number, it will output the corresponding value of 'r'.
#'r' signafies the amount of numbers following the user input that added to equal the sum.

#Variables assigning input and starting calculation values
n_input = int(input("Enter a value for n: "))
r = 0
n_sum = 0
n_sum_2 = 0
n_start = n_input

#for loop specifying the range from user input to 0.
for n_calculation in range(n_input, 0, -1):
    #Calculate the arithmetic series sum based on a starting value from user input.
    n_sum += n_calculation

#Continue to check if a sum of the following numbers after user input is greater than or equal to the sum of arithmetic series. 
while n_sum_2 < n_sum:
    #Calculate the sum of numbers following the user input
    #Example: 14 + 15 + 16...
    n_start += 1
    n_sum_2 += n_start

    #Trace how many times this loop runs. The amount of times it runs can be used as value r.
    #r signafies the amount of numbers following the user input that added to equal the sum
    r += 1

#Check if the first sum of the arithmetic sequence is equal to the second sum.
if n_sum == n_sum_2:
    #printing user input is a co-balancing number.
    print(f'{n_input} is a co-balancing number with r={r}')

#if the condition is false, the number is not a co-balancing number.
else:
    print(f'{n_input} is not a co-balancing number')
