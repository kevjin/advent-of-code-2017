#Got lucky cause while I was coding, noticed the answer was on the rightmost vertical vector of the matrix

upperRight = 3
index = 1 #one location from center
answer = 361527
additive = 2
while(answer > upperRight):
	additive+=8
	upperRight +=additive
	index+=1
print "index: " +  str(index)
saveIndex = index
print "remainder: " + str(upperRight - answer)

newAdd = 1
horizRight = 2
while(index>1):
	index-=1
	newAdd+=8
	horizRight+=newAdd
print "horiz: " + str(horizRight)
print("diff: " + str(answer - horizRight))

numberofSpaces = answer - horizRight + saveIndex
print ("Answer: " + numberofSpaces)