'''
l = []
for i in range(10):
    a = input("Enter the list:")
    b = input("Enter the position:")
    l.insert(int(b),int(a))
print(l)
'''
'''
a = input("Enter the length:")
d = input("Enter Numbers: ").split()
d = list(set(d))
print(d)
#d = map(int, d)
#print(d)
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = sorted(set(arr))
    print(arr)
    print(arr[-2])
