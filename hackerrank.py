'''
def mutate_string(string, position, character):
#    string = s
    l = list(string)
    l[position] = character
    string =''.join(l)
    return string


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s,int(i), c)
    print(s_new)
def count_substring(string, sub_string):
    s = string.count(sub_string)
    return s

if __name__ == '__main__':
    string = input().strip()
    print(string)
    sub_string = input().split()
    count = count_substring(string,sub_string)
    print(count)

'''    
'''
n = input("Input:")
if len(n) < 0 or len(n) > 1000:
    print("Length is less or More")
    sys.exit()

if (any(i.isalnum() for i in n)): 
    print("True") 
else: 
    print("False")

if (any(i.isalpha() for i in n)):
    print("True")
else:
    print("False")
if (any(i.isdigit() for i in n)):
    print("True")
else:
    print("False")
if (any(i.islower() for i in n)):
    print("True")
else:
    print("False")

if (any(i.isupper() for i in n)):
    print("True")
else:
    print("False")
def leapyr(year):
    if year % 4 == 0: 
        leap =  True
        if year % 100 == 0 and year % 400 !=0:
            leap =  False
            return leap
        else:
            leap = True
            return leap
    else:
        leap = False
        return leap

year = int(input())
print(leapyr(year))
'''

totalcust = int(input())
showlist = list(input().split())
custnum = int(input())
if len(showlist) > 10:
    print("Length of the array exceeds 10")
    sys.exit()
d = {}    
for i in range(custnum):
    size, amt = map(int, input().split())
    print(size)
    print(amt)
    d[size].append(amt) 
    print(d)
print(showlist)
