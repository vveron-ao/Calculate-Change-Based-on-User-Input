#The purpose of this program is to prompt the user to enter 2 integers. It will output the numbers 1 to 100, each on its own line, unless the number is evenly divisible by one or both of the integers entered by the user. 
#If the number is evenly divisible by the first integer, print Howdy. If it’s evenly divisible by the second integer, print Whoop. If it’s evenly divisible by both, print Howdy Whoop.

#Variables
integer_1 = int(input("Enter an integer: "))
integer_2 = int(input("Enter another integer: "))

#For loop specifying the range of 1-100
for num_range in range(1, 101):

#If statements applying conditions for even divisiability
    #if any number 1 - 100 is evenly divisible by both inputs, run this code
    if ((num_range % integer_1) == 0) and ((num_range % integer_2) == 0):
        print("Howdy Whoop")

    #Only run this code if any number 1 - 100 is only divisible by the 1st input
    elif (num_range % integer_1) == 0:
        print("Howdy")

    #Only run this code if any number 1 - 100 is only divisible by the 2nd input
    elif (num_range % integer_2) == 0:
        print("Whoop")

    #This will print all numbers that aren't evenly divisible by either of the inputs.
    else:
        print(num_range)
