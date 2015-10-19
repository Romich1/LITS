import random

def makecardslist(lstlears,lstcards):
	
	lst = []

	for mast in lstlears: 
		for card in lstcards:
			lst.append(mast+card)

	return lst


def randomcardfromlst(lstfrom,lstto,amount):
	
	amount = min(amount,len(lstfrom)) 
	
	if amount == 0:
		return False
	
	rndcard = random.choice(lstfrom) 
	lstto.append(rndcard)
	lstfrom.remove(rndcard)

	if amount > 1:
		randomcardfromlst(lstfrom,lstto,amount-1) 

	return True


def makestep(lstfrom,playlist,trumpcard): 

	if len(playlist) == 0: # firs step:
		pass
	
	if len(lstfrom) != 0:				
		card = random.choice(lstfrom);
		playlist.append(card)
		lstfrom.remove(card)		
		return True		
	else: 
		return False

		
def answerstep(lstfrom,playlist,trumpcard):

	randomize = random.random()
	
	if len(lstfrom) != 0:
		if randomize > 0.2:
			card = random.choice(lstfrom);
			playlist.append(card)
			lstfrom.remove(card)
			return True			
		else:	
			lstfrom.extend(playlist)
			return False
	else: 
		return True

		
print('============================================')
		
lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

lst = makecardslist(lstlears,lstcards)

mycards = []
compcards = []
playlist = []

randomcardfromlst(lst,mycards,6);
randomcardfromlst(lst,compcards,6);

trumpcard = lst[len(lst)-1]

direction = True

while len(compcards) != 0 and len(mycards) != 0:
	
	if direction:
		makestep(mycards,playlist,trumpcard)	
		direction = not answerstep(compcards,playlist,trumpcard)
	else:	
		makestep(compcards,playlist,trumpcard) 
		direction = answerstep(mycards,playlist,trumpcard)  
	
	playlist = []
	
	randomcardfromlst(lst,mycards,max(6-len(mycards),0));
	randomcardfromlst(lst,compcards,max(6-len(compcards),0));
	
	print('\nmy - '+str(len(mycards))+' '+str(mycards))
	print('comp - '+str(len(compcards))+' '+str(compcards))
	print('lst - '+str(len(lst))+' '+str(lst))


print('\n------------------------')

# print(mycards)
# print(compcards)
# print(lst)
# print(len(lst))
# print(trumpcard)
