TheList = [int(x) for x in input("Dwse ari8mous xwrismenous me kena: "). split()]
for i in TheList:
	if(i==0):
		TheList.remove(i)
		TheList.append(0)
print (TheList)
