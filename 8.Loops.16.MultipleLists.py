'''
8.Loops -> 16.Multiple lists
It is common to need to iterate over two lists at once. This is where the built-in function zip comes in handy.
zip can create pairs of elements when passed two lists, and will stop at the end of the shorer list.
zip can handle three or more lists as well.
Instructions: 
Compare each pair of element and print the larger of the two.
Hint:
a is an element from list_a and b is an element from list_b. Use an if statement to compare the two and print whichever is larger.

Oct 21, 2016; worked; 8.Loops.16.MultipleLists.py

'''
list_a = [3,9,17,15,19]
list_b = [2,4,8,10,39,40,50,60,70,80,90]

for a,b in zip(list_a, list_b):
  if a >= b:
    print a
  else:
    print b
