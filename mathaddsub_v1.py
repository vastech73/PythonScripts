import webbrowser,os,random
import time,emoji
start_time = time.time()

def addnum(ques,num1,num2):

    #os.system('clear')

    print(ques, ": Addition")
    print("______________\n")
    print( num1)
    print("+")
    print( num2)
    print("==")
    ans = int(input())

    if ans == num1 + num2:
        #print(emoji.emojize(':thumbsup:', use_aliases=True))
        return True, ans 
    else:
        #print(emoji.emojize(':thumbsdown:', use_aliases=True))
        ans = num1 + num2 
        return False, ans 

count = 0
errcount = 0
answer = []
wrong = []
for i in range(1,11):
    val, ans = addnum("Q%s" %i,random.randrange(1,1000,100),random.randrange(1,2000,100))
    if val:
        count += 1
        answer.append(ans)
    else:
        print("Answer for Q%s is: %s" %(i, ans))
        wrong.append(ans)
        errcount += 1

end_time = time.time() - start_time
print("Time taken: %f \n" %  end_time)

print("Answer Report")
print("------------- \n")
print("Correct answers: %s" % answer)
print("Wrong answers: %s" % wrong)
tup = 0
tdn = 0
while (tup < len(answer)):
        print(emoji.emojize(':thumbsup: \n', use_aliases=True))
        tup += 1
while (tdn < len(wrong)):
        print(emoji.emojize(':thumbsdown: \n', use_aliases=True))
        tdn += 1
if count == 10:
   #for r in range(1,6):
   #     print("Answer for Q%s: %s" % (r, answer[r-1]))
   #     print(emoji.emojize(':thumbsup:', use_aliases=True))

   time.sleep(5)
   webbrowser.open('https://www.youtube.com/watch?v=jmIM5txH0oM')
elif count < 5:
   print("No of answers correct %s" % count)
   print("No of wrong  answers %s" % errcount)
   #print("You can do Better: %s" % name)

time.sleep(5)
# Multiplication Problems
def mulnum(ques,num1,num2):

    #os.system('clear')
    print(ques, ": Multiplication ")
    print("----------------------------")
    print(num1)
    print("*")
    print(num2)
    print("==")
    ans = int(input())

    if ans == num1 * num2:
        return True, ans 
    else:
        ans = num1 * num2
        return False, ans

start_time = time.time()
count = 0
errcount = 0
answer = []
wrong = []
#name = str(input("What is your name young man?:"))
'''
for i in range(1,11):
    val, ans = mulnum("Q%s" %i,random.randrange(1,10,1),random.randrange(2,10,2))
    if val:
        count += 1
        answer.append(ans)
    else:
        print("Answer for Q%s is: %s" %(i, ans))
        wrong.append(ans)
        errcount += 1

end_time = time.time() - start_time
print("Time taken: %f \n" %  end_time)

print("Answer Report")
print("------------- \n")
print("Correct answers: %s" % answer)
print("Wrong answers: %s" % wrong)
tup = 0
tdn = 0
while (tup < len(answer)):
        print(emoji.emojize(':thumbsup: \n', use_aliases=True))
        tup += 1
while (tdn < len(wrong)):
        print(emoji.emojize(':thumbsdown: \n', use_aliases=True))
        tdn += 1
if count == 10:
   #print("You are Great: %s" % name)
   time.sleep(5)
   webbrowser.open('https://www.youtube.com/watch?v=jmIM5txH0oM')
elif count < 10:
    print("No of answers correct %s" % count)
    #print("You can do Better: %s" % name)
'''
