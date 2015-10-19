
def factorylist(lstint,element,amountint): 
	
	lstint.append(str(element))
	element += 1;

	if amountint > 1:
		factorylist(lstint,element,amountint-1)
	
	return lstint


lst = []
newlst = factorylist(lst,1,9) 
print(newlst)
