'''
Python program to find the duplicate number in a list
'''

def find_duplicates(lst):
	dup_val_lst = []
	for i in range(1,len(lst)):
		k = i - 1 
		if lst[k] == lst[i]:
			dup_val_lst.append(lst[i])
	return dup_val_lst




lst = [45,45,100,78,78,34,34,2,1,230,230]
print(find_duplicates(lst))
