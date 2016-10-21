'''
8.Loops.17.For / Else

For / else
Just like with while, for loops may have an else associated with them.
In this case, the else statement is executed after the for, but only if the for ends normally—that is, not with a break. This code will break when it hits 'tomato', so the else block won't be executed.

Instructions
Click Save & Submit Code to see how for and else work together.

CN-codedemy-script-8.Loops.17.ForElse.py
Oct 21, 2016: worked
Tested 3 cases:
fruits = ['banana', 'apple','orange','tomato','pear','grape'] -> Output:
You have ...
A banana
A apple
A orange
A tomato is not a fruit!

fruits = ['banana', 'apple','orange','pear','grape'] -> Output:
You have...
A banana
A apple
A orange
A pear
A grape
A fine selection of fruits!

fruits = ['tomato', 'banana', 'apple','orange','pear','grape'] -> Output:
A tomato is not a fruit!
'''
# fruits = ['banana', 'apple','orange','tomato','pear','grape']
fruits = ['banana', 'apple, 'orange']
# fruits = ['tomato','banana']

print 'You have ...'
for f in fruits:
  if f == 'tomato':
    print "A tomato is not a fruit!' # Is it or is it not?
    break
  print 'A', f # 'A' is for A <fruit>  
else:
  print 'A fine selection of fruits' # This line will be printed when the "for" loop exits naturally

