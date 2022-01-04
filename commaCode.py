'''
# commaCode.py
Write a function that takes a list value as an argument and returns a string with all the items
separated by a comma and a space, with and inserted before the last item. 
Example: spam = ['apples', 'bananas', 'tofu', 'cats'] would return 'apples, bananas, tofu, and cats'
'''

listValues = ['apples', 'bananas', 'tofu', 'cats']

def commaCode(items):
	items[-1] = 'and ' + items[-1]
	print(', '.join(items))

commaCode(listValues)
