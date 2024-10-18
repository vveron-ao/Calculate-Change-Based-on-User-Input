#This Python code prompts the user to input the coefficients AAA, BBB, and CCC for a quadratic equation of the form Ax2+Bx+C=0Ax^2 + Bx + C = 0Ax2+Bx+C=0. It then assembles the quadratic equation string based on these inputs, ensuring correct formatting for positive, negative, and zero #values. If all inputs are zero, the program flags the input as invalid. Finally, it prints the resulting quadratic equation in the proper mathematical format.


#First we will define our coefficients by prompting the user to input values.
A = int(input("Please enter the coefficient A: "))
B = int(input("Please enter the coefficient B: "))
C = int(input("Please enter the coefficient C: "))
#Now we will assess the values to make sure they do not ALL equal zero.
if A == 0 and B == 0 and C == 0:
    print("Invalid input, please use nonzero integers.")
#We will now start evaluating all other cases of inputs
else:
    #This variable is how we will define our equation, we will start with an empty string.
    quadratic = ""
#We will now evaluate the input for A and define the start of our equation.
    if A != 0:
        if A == 1:
            quadratic = (" x^2 ")
        elif A == -1:
            quadratic = (" - x^2")
        elif A > 0:
            if quadratic:
                quadratic = (f" {A}x^2 ")
            else:
                quadratic = (f" {A}x^2 ")
        else:
            if quadratic:
                quadratic += (f" {A}x^2 ")
            else:
                quadratic = (f" - {abs(A)}x^2 ")
                
            
#We will now evaluate the input for B and use the += function to add the correct format
#To the equation depending on positive or negative values.
    if B != 0:
        if B == 1:
            if quadratic:
                quadratic += ("+ x ")
            else:
                quadratic = (" x ")
        elif B == -1:
            if quadratic:
                quadratic += ("- x ")
            else:
                quadratic = ("- x ")
        #This else statement will evaluate cases when B does not equal 1, or -1.
        elif B > 0:
            if quadratic:
                    quadratic += (f"+ {B}x ")
            else:
                    quadratic = (f" {B}x ")
        else:
            if quadratic:
                    quadratic += (f" - {-B}x ")
            else:
                    quadratic = (f" - {-B}x ")
   # Finally we will assess the cases for C and add correctly formatted input to the equatin.
    if C != 0:
        if C > 0:
            if quadratic:
                quadratic += (f"+ {C} ")
            else:
                quadratic = (f"{C} ")
        else:
            if quadratic:
                quadratic += (f"- {-C} ")
                
    print(f'The quadratic equation is{quadratic}= 0')
            #These if statements check if the string variable for the equation is empty
            #and if so adds the correct value to it.
