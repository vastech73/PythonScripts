from datetime import datetime
'''
N = int(input())
l = list(map(int, input().split()))
count = 0
for i in l:
    if i >= 0 and i <= N:
        count += 1
if count == len(l):        
    print("YES")
else:
    print("NO")
startTime = datetime.now()
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        print("First val:",numList[0])
        print("Array:",numList[1:])
        return numList[0] * listsum(numList[1:])
print(listsum([1,3,5,7,9,10,11,2,13,14]))
print(datetime.now() - startTime)
startTime = datetime.now()
def listsum(numList):
    theSum = 0
    for i in numList:
        theSum = theSum + i
    return theSum

print(listsum([1,3,5,7,9,10,11,12,13,14]))
print(datetime.now() - startTime)
'''
array = []
numarr = []
array = input().split()
chknum = array[1]
int(chknum)
print(chknum)
numarr = map(int, input().split())
print(numarr)
addnum = 0
for i in numarr:
    addnum = addnum + i 
    print(addnum)
    if addnum == chknum:
       print("YES")

