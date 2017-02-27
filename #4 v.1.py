import math

list = [int(x) for x in input("Dwse ari8mous xwrismenous me kena: ").split()]
del list[-1]
del list[-1]
del list[0]
del list[0]
if (len(list)>0):
	sum=0
	for i in range(len(list)):
		sum+=list[i]
	MO= sum/len(list)
	sum=0
	for i in range(len(list)):
		dis=math.fabs(list[i] - MO)
		sum+=math.pow(dis,2)
	ds=math.sqrt(sum/len(list))
	print (ds)
else:
	print ("Eipa dwse ari8mous...")
#for checking the program
#print (list)
