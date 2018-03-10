'''
Python Program to add the values in a list
'''


def add_lst(lst):
	temp_list = 0 
	for i in range(len(lst)):
		temp_list += lst[i]
	return temp_list


lst = [3,56,78,90]
print(add_lst(lst))
