def DigitSum(n):
	dig = list(str(n))
	sum = 0
	for i in dig:
		sum += int(i)
	return sum

def DigitProduct(n):
	dig = list(str(n))
	prod = 1
	for i in dig:
		if(int(i)!=0):
			prod *= int(i)
	return prod
	
	
print("Harshad numbers from 0 to 1000")
for n in range(1,1001):
	if (n%DigitSum(n)==0):
		print(n)
#Emfanish ari8mwn pou diairountai apo to ginomeno psifiwn
print ("Those other numbers requested")
for n in range(1, 1001):
	if (n%DigitProduct(n)==0):
		print (n)
