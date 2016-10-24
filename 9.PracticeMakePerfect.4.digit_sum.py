'''
Try summing the digits of a number.
Instructions
Write a function called digit_sum that takes a positive integer number's digits.
For example: digit_sum(1234)should return 10 which is 1 + 2 + 3 + 4.
(Assume that the number you are given will always be positive.)
Check the hint if you need help!

One way might be to convert the integer to a string with str(), divide it up, and turn the substrings back into integers with int() to do the addition.
If you're looking for a challenge, try this: to get the rightmost digit of a number, you can modulo (%) the number by 10. To remove the rightmost digit you can floor divide (//) the number by 10. (Don't worry if you're not familiar with floor division—you can look up the documentation here. Remember, this is a challenge!)
Try working this into a pattern to isolate all of the digits and add them to a total.
n as input and returns the sum of all that 

9.Practice Make Perfect.4.digit_sum
CN-codedemy-script-9.Practice-4.digit_sum.py
Oct 21, 2016 worked
No output
'''

def digit_sum():
  num_as_str = str(n)
  num_as_list = []
  total = 0
  for i in range(len(num_as_str)):
    temp = num_as_str[i]
    total += int(temp)
  return total
