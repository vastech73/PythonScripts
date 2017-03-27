# If else operation
'''
inp = input("Enter the number:")
if (int(inp) % 2) == 1:
    print("Weird")
elif int(inp) % 2 == 0 and int(inp) >= 2 and int(inp) <= 5:
    print("Not Weird")
elif int(inp) % 2 == 0 and int(inp) >= 6 and int(inp) <= 20:
    print("Weird")
elif int(inp) % 2 == 0 and int(inp) > 20:
    print("Not Weird")
a = int(input("Enter 1st No:"))
b = int(input("Enter 2nd No:"))
print(10**10)
if (a >= 1 and a <= 10**10) and (b >= 1 and b <= 10**10):
    print(a + b)
    print(a - b)
    print(a * b)
a = int(input("Enter 1st No:"))
b = int(input("Enter 2nd No:"))
print(a//b)
print(a/b)

a = int(input("No:"))
if a >= 1 and a <= 20:
    for i in range(0,a):
        print(i*i)

list = []

a = int(input("Enter No:"))

list.insert(a,a)
print(list)
'''
n = int(input("Enter No"))
integer_list = map(int,input().split())
t = ()
t += tuple(integer_list)
print(t)
print(hash(t))


