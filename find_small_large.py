'''
Python program to find the smallest & largest number in a list
The list is not sorted
valtype = 0 looks for smallest number in the list
valtype = 1 looks for largest number in the list
'''

def find_small_large(lst,valtype=0):
	minimum = lst[0]
	maximum = lst[0]
	if valtype == 0:
		for i in range(1,len(lst)):
			if lst[i] < minimum:
				minimum = lst[i]
				#print('Inside loop:{}'.format(minimum))
		return minimum
	elif valtype == 1:
		for i in range(1,len(lst)):
			if lst[i] > maximum:
				maximum = lst[i]
		return maximum





lst = [45,100,78,34,4,2,1,230]
print(find_small_large(lst,1))
