# Recursive Fibonacci Sequence Generator in Python
# Written by Danielle O'Sullivan
# Credit me if you use my code

def FibGen(number):
  FibList = []
  curr = 0 # Number to work out
  prev1 = 0 # One number previous to current
  prev2 = 0 # Two numbers previous to current

  for i in range(1, number): 
    if i == 1:
      FibList.append(curr) # Adds 0 to list
      curr = curr + 1 # Updates current number
      FibList.append(curr) # Adds new current number to list
      prev2 = prev1 # Updates last two numbers
      prev1 = curr
    else:
      curr = prev2 + prev1 # Updates current number
      FibList.append(curr) # Adds new current number to list
      prev2 = prev1
      prev1 = curr # Updates last two numbers
  
  print FibList
  

while True:
  try:
    # Attempt to change string input to integer input
    number = int(raw_input("How many Fibonacci numbers do you want to see?"))
  except ValueError:
    # If invalid input is received
    print "Sorry, I did not understand that input, please input a whole number."
    # Restarts loop
    continue
  if number <= 0:
    # Need to check if number is negative
    print "Sorry, seems like that is not a positive integer, try again please."
    continue
  else:
    # Successful parse of input
    print "Producing %s Fibonacci numbers..." % number
    # Calls function
    FibGen(number)
    break
