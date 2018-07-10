'''
Build a smart math equivalent solution with the following features:
Arithmetic Solution:
	* Addition
	* Subtraction
	* Multiplication
	* Division
Page Offering:
	* Page for Addition
	* Page for Subtraction
	* Page for Multiplication
	* Page for Division

Front end should have [Prev] & [Next] event click to move to the prevous/next pages
Submit button in the last page
'''
from prettytable import PrettyTable
results_table = PrettyTable(['Question', 'Correct Answer', 'Your Answer','Result'])
results_table.align["Question"] = "l"
import random
import emoji,os

res = []
add_dict = {}
add_sub_num_lst = [5,10,20,100]
mul_num_lst = [2,3,4,5,6,7,8,9,10]
rand_lst = ['add_num','sub_num','mul_num']


def gen_num(fn_type,num,fn_val):
	if fn_type == 'add_num':
		print('Add the following Number:')
		print('{} + {}'.format(num,fn_val))
	elif fn_type == 'sub_num':
		print('Subtract the following Number:')
		print('{} - {}'.format(num,fn_val))
	elif fn_type == 'mul_num':
		print('Multiply the following Number:')
		print('{} x {}'.format(num,fn_val))
	ans = int(input())
	return ans


def score_report(dict):
	pass_count = 0
	fail_count = 0
	total_count = len(dict)
	#for i in dict.values():
	for i in dict:
		#if i[0]==i[1]:
		if dict[i][0] == dict[i][1]:
			pass_count += 1
			results_table.add_row([i,dict[i][1],dict[i][0],'PASS'])
		else:
			fail_count += 1
			results_table.add_row([i,dict[i][1],dict[i][0],'FAIL'])
	print('Pass % {}'.format((pass_count/total_count)* 100))
	print(results_table)
	#for i in dict.keys():
	# print('Detailed report')
	# for j in dict:
	#     print('Q{}:\n Your Answer: {}\n Correct Answer: {}'.format(j,dict[j][1],dict[j][0]))

fn_type = random.choice(rand_lst)

''' Single/Two/Three Digit Addition '''
def add_num(digit):
	for i in range(1,20):
		if digit == 'single':
			num = random.randrange(0,9)
			fn_val = random.randrange(0,9)
		elif digit == 'two':
			num = random.randrange(10,99)
			fn_val = random.randrange(10,99)
		elif digit == 'three':
			num = random.randrange(100,999)
			fn_val = random.randrange(100,999)
		fn_type = 'add_num'
		ret_val = gen_num(fn_type,num,fn_val)
		add_dict.update({i: [num + fn_val, ret_val]})
	score_report(add_dict)

''' Single/Two/Three Digit Subtraction '''
def sub_num(digit):
	for i in range(1,20):
		if digit == 'single':
			num = random.randrange(0,9)
			fn_val = random.randrange(0,9)
		elif digit == 'two':
			num = random.randrange(10,99)
			fn_val = random.randrange(10,99)
		elif digit == 'three':
			num = random.randrange(100,999)
			fn_val = random.randrange(100,999)
		fn_type = 'sub_num'
		ret_val = gen_num(fn_type,num,fn_val)
		add_dict.update({i: [num - fn_val, ret_val]})
	score_report(add_dict)

''' Single/Two/Three Digit Multiplication '''
def mul_num(digit):
	for i in range(1,20):
		if digit == 'single':
			num = random.randrange(0,9)
			fn_val = random.randrange(0,9)
		elif digit == 'two':
			num = random.randrange(10,99)
			fn_val = random.randrange(10,99)
		elif digit == 'three':
			num = random.randrange(100,999)
			fn_val = random.randrange(100,999)
		fn_type = 'mul_num'
		ret_val = gen_num(fn_type,num,fn_val)
		add_dict.update({i: [num * fn_val, ret_val]})
	score_report(add_dict)

''' Random Smart math method '''
def random_add_sub_mul():
	for i in range(1,5):
		num = random.randrange(0,500)
		if fn_type == 'mul_num':
			fn_val = random.choice(mul_num_lst)
		else:
			fn_val = random.choice(add_sub_num_lst)
		ret_val = gen_num(fn_type,num,fn_val)
		if fn_type == 'add_num':
			add_dict.update({i: [num + fn_val, ret_val]})
		elif fn_type == 'sub_num':
			add_dict.update({i: [num - fn_val, ret_val]})
		else:
			add_dict.update({i: [num * fn_val, ret_val]})
	score_report(add_dict)

print('****************************')
print('* Welcome to MathPrac      *')
print('* Author: Vasudevan V      *')
print('****************************\n')
print('Enter one of the option')
print('-----------------------\n')
print('1.Addition')
print('2.Subtraction')
print('3.Multiplication')
print('4.Random Add/Sub/Mul')
opt = str(input('Enter the Option:'))
os.system('clear')
if opt == '1':
	print('1.Single Digit Addition')
	print('2.Two Digit Addition')
	print('3.Three Digit Addition')
	opt_add = str(input('Enter the Option for Addition:'))
	if opt_add == '1':
		os.system('clear')
		add_num('single')
	elif opt_add == '2':
		os.system('clear')
		add_num('two')
	elif opt_add == '3':
		os.system('clear')
		add_num('three')
	else:
		print('Please Enter the Correct Option for Addition!')
elif opt == '2':
	print('1.Single Digit Subtraction')
	print('2.Two Digit Subtraction')
	print('3.Three Digit Subtraction')
	opt_sub = str(input('Enter the Option for Subtraction:'))
	if opt_sub == '1':
		os.system('clear')
		sub_num('one')
	elif opt_sub == '2':
		os.system('clear')
		sub_num('two')
	elif opt_sub == '3':
		os.system('clear')
		sub_num('three')
	else:
		print('Please Enter the Correct Option for Subtraction!')
elif opt == '3':
	print('1.Single Digit Multiplication')
	print('2.Two Digit Multiplication')
	print('3.Three Digit Multiplication')
	opt_mul = str(input('Enter the Option for Multiplication:'))
	if opt_mul == '1':
		os.system('clear')
		mul_num('one')
	elif opt_mul == '2':
		mul_num('two')
	elif opt_mul == '3':
		mul_num('three')
	else:
		print('Please Enter the Correct Option for Multiplication!')
elif opt =='4':
	os.system('clear')
	random_add_sub_mul()
