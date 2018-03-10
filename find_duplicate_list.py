def find_missing(lst,array_size):
	array_sum = sum(lst)
	array_sum_orig = array_size * (array_size + 1) / 2
	print("Sum of given array:{}".format( array_sum))
	print('Sum of Original array:{}'.format(array_sum_orig))
	missing_number = array_sum_orig - array_sum
	if len(lst) > array_size:
		missing_number = array_sum - array_sum_orig
	return missing_number


lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,19,20]

print(find_missing(lst,20))
