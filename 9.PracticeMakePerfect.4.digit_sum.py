'''
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
