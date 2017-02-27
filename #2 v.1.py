#h sunarthsh proper() kaleitai gia ka8e stoixeio pou plhktrologei o xrhsths. O xrhsths prepei na plhktrologhsei mono paren8eseis
def proper(i, test):
	if (paren[i]=="(" or paren[i]==")" or paren[i]==" "):
		if (test>=0):
			if (paren[i] == "("):
				i+=1
				test+=1
				#anadromikh xrhsh ths proper()
				test=proper(i, test)
				return test
			elif(paren[i]==")"):
				i+=1
				test-=1
				test=proper(i, test)
				return test
	else:
		test=-1
	return test
		


paren = input("Dwse parentheseis:")
#For testing the program
#print(paren)
test=0
i=0
paren+=" "
test = proper(i, test)
if (test!=0):
	print("False")
else:
	print("True")
#For testing the program
#print (test)

