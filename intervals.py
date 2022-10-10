from itertools import count
from typing import overload
from venv import create


lists = [
   [1,4],
   [7, 10],
   [3, 5],
]



def sumIntervals(interval):
    noOverlap = 0
    overlapPeak = interval[0][1]
    overlapBottom = interval[0][0]
    overlapPeak = 0
    for x in range (len(interval)):
        overlap = (interval[x][1] - interval[x][0])
        intervalLen = len(interval)
        

        listTest = interval[x]
        listTestfirst = listTest[:1]
        overlappingIndex = []
        print(x)
        if x not in overlappingIndex:

            for i in range (len(interval)):
                print(" interval testing now " +str(interval[i]))
                print(" listtest testing now " +str(listTest[i]))
                if(listTest[0] == interval[i][0] and listTest[1] == interval[i][1]):
                    print("testing myself")
                elif(listTest[0] < interval[i][0]) and (interval[i][0] <= listTest[1] <= interval[i][1]):
                    print("we have an overlap here")
                    overlappingIndex.append(i) if i not in overlappingIndex else overlappingIndex
                    if(overlapPeak < interval[i][1]):
                        overlapPeak = interval[i][1] 
                        overlapBottom = list[0]
                else:
                    noOverlap += (interval[i][1] - interval[i][0])
                    break
        totalOverlap = (overlapPeak - overlapBottom) + noOverlap
        print(totalOverlap)

sumIntervals(lists)







        

    


