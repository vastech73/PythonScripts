import time,webbrowser,os
import random
start_time = time.time()
def addnum(ques,num1,num2):

   os.system('clear')

   print("Add the given Number: ",ques)
   print("____________________ ")
   print( num1)
   print("+")
   print( num2)
   print("==")
   ans = int(input())

   if ans == num1 + num2:
        return True, ans
   else:
        return False

count = 0
errcount = 0
answer = []
for i in range(1,5):
    val, ans = addnum("Q%s" %i,random.randrange(1,20,2),random.randrange(2,30,3))
    print(val,ans)
    if val:
       count += 1
       answer.append(ans)
    else:
        print("Answer for Q%s is :" %i)
        errcount += 1

print(time.time() - start_time)
print(answer)
print("Answer Report")
for r in range(1,5):
    print("Answer for Q%s: %s" % (r, answer[r-1]))
'''
if count == 10:
        print("All answers COrrect")
        #print("You can do Better: %s" % name)
        time.sleep(5)
        webbrowser.open('http://ndtv.com')
elif count < 10:
        print("No of answers correct %s" % count)
        print("No of wrong  answers %s" % errcount)
        print("You can do Better: %s" % name)
'''
