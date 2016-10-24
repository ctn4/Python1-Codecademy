'''
9.Practice Makes Perfect.5.Factorial.py
'''
'''
Solution 1
Oct 24, 2016 worked as expected
'''
def factorial(x):
  if x == 1:
    return 1
  else:
    return x * factorial(x - 1)
    
user_input_str = raw_input("Please enter an integer: ")
print factorial((int(user_input_str)))




'''
Solution 2:
Oct 24, 2016 worked but this is not what the execirse asked
import math
def factorial(x):
  return math.factorial(x)

user_input_str = raw_input("Please enter an integer: ")
print factorial((int(user_input_str)))
'''
