#text_file = open("stringmatch.txt", "w")

#for i in range(1,60000):
#    text_file.write("%PKT_INFRA-LINEPROTO-5-UPDOWN %ROUTING-ISIS-5-ADJCHANGE %L2-BFD-6-SESSION_REMOVED\n")

#text_file.close()
import time
start_time = time.time()
count = 0
with open('stringmatch.txt', 'r') as searchfile:
    for line in searchfile:
        if "%PXT_INFRA-LINEPROTO-5-UPDOWN %ROUTING-ISIS-5-ADJCHANGE %L2-BFD-6-SESSION_REMOVED" in line  or  "%PKT_INFRA-LINEPROTO-5-UPDOWN %ROUTING-ISIS-5-ADJCHANGE %L2-BFD-6-SESSION_REMOVED" in line or  "%PKT_INFR-LINEPROTO-5-UPDOWN %ROUTING-ISIS-5-ADJCHANGE %L2-BFD-6-SESSION_REMOVED" in line:
            count += 1
        else:
            print("Match Not found")
            #print(line)

print("--- %s seconds ---" % (time.time() - start_time))
print(count)

