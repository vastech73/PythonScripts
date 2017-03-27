def li(a):
  for val in a:
    if 0 in a:
       a.remove(0)
       a.append(0)
  for i in range(0,len(a)-1):
     if a[i] == a[i+1]:
         a[i] = a[i] + a[i+1]
         print a[i]
         for r in range(i+1,len(a)-1):
             a[r] = a[r+1]
         a[len(a)-1] = 0
  print a
  return(a)

a = [4,4,0,2]
li(a)
