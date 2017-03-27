#with open("f1.txt",'w') as d:
#  for line1 in d:
#        with open("filematch.txt",'r') as f:
#            for line2 in f:
#                if line2 in line1:
#                    break
#                else:
#                    newFile.write (line2)
#        newFile.close()

lines_seen = set() # holds lines already seen
outfile = open("f1.txt", "w")
for line in open("filematch.txt", "r"):
        if line not in lines_seen: # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
outfile.close()
