from math import *
quarter = 25
dime = 10
nickel = 5
penny = 1
paid_input = (input("How much did you pay? \n"))
cost_input = (input("How much did it cost? \n"))

cost_input = float(cost_input)
paid_input = float(paid_input)
cost_input = int(cost_input * 100)
paid_input = int(paid_input * 100)

#subtract amt paid from amt cost
change = int(paid_input - cost_input)

change = paid_input - cost_input
if paid_input < cost_input:
   print(f'You did not pay enough. You need to pay ${((cost_input - paid_input))/100:.2f} more.')
else:
   print(f"You received ${change/100:.2f} in change. That is... \n")

#filter quarters
if (change // 25) >= 1:
   if (change // 25) == 1:
       print(f"{change // 25} quarter")
   else:
       print(f"{change // 25} quarters")
  
   change = int(change - ((change // 25) * 25))

#filter dime
if (change // 10) >= 1:
   if (change // 10) == 1:
       print(f"{change // 10} dime")
   else:
       print(f"{change // 10} dimes")
  
   change = int(change - ((change // 10) * 10))

#filter nickel
if (change // 5) >= 1:
   if (change // 5) == 1:
       print(f"{change // 5} nickel")
   else:
       print(f"{change // 5} nickels")
   change = int(change - ((change // 5) * 5))

#filter pennies
if (change // 1) >= 1:
   if (change // 1) == 1:
       print(f"{change // 1} penny")
   else:
       print(f"{change // 1} pennies")
