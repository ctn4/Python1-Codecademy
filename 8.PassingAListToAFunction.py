'''
Passing a list to a function
You pass a list to a function the same way you pass any other argument to a function.
'''
def list_function(x):
	return x
n = [3, 5, 7]	
print list_function(n)
# see [3, 5, 7]	

'''
9.Using an element from a list in a function
Passing a list to a function will store it in the argument (just like with a string or a number!)
def first_item(items):
	print items[0]
numbers = [2, 7, 9]
first_item(numbers)
'''
def list_function(x):
	return x[1]
n = [3, 5, 7]
print list_function(n)
# see 5	
