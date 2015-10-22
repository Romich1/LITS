import random

def sotrlist(lstincome):
	
	trumplist = []
	cardslist = []
	
	for i in lstincome: 
		if i[0] == trumpcard[0]: 
			trumplist.append(i)
		else:
			cardslist.append(i)
	
	print(cardslist)
	print(trumplist)
			

def makecardslist(lstlears,lstcards):
	
	lst = []

	for mast in lstlears: 
		for card in lstcards:
			lst.append(mast+card)

	return lst

#takes card from list. 
#next card if randomchoice = False 
#random card if randomchoice = True 	
def cardfromlst(lstfrom,lstto,amount,randomchoice=False):

	amount = min(amount,len(lstfrom)) 

	if amount < 1: 
		return False
	
	if randomchoice: 
		card = random.choice(lstfrom) 
	else:
		card = lstfrom[0]
		
	lstto.append(card)
	lstfrom.remove(card)

	if amount > 1:
		cardfromlst(lstfrom,lstto,amount-1,randomchoice) 

	return True

#return shufled list from recieved one
def shufflecards(lsttoshuffle):
	
	lstshuffled = [] 
	cardfromlst(lsttoshuffle,lstshuffled,len(lsttoshuffle),True)	

	return lstshuffled
	
#move
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

#countermove		
def answerstep(lstfrom,playlist,trumpcard):

	randomize = random.random()
	
	if len(lstfrom) != 0:
		if randomize > 0.4:
			card = random.choice(lstfrom);
			playlist.append(card)
			lstfrom.remove(card)
			return True			
		else:	
			lstfrom.extend(playlist)
			return False
	else: 
		return True


def printstatus(mycards,compcards,lst):
	
	print('\nmy - '+str(len(mycards))+' '+str(mycards))
	print('comp - '+str(len(compcards))+' '+str(compcards))
	print('lst - '+str(len(lst))+' '+str(lst))
		
			
print('============================================')
		
lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

lstnew = makecardslist(lstlears,lstcards)
lst = shufflecards(lstnew) 

mycards = []
compcards = []
playlist = [] #list of current game session (before pass out)

cardfromlst(lst,mycards,6-len(mycards))
cardfromlst(lst,compcards,6-len(compcards))

trumpcard = lst[len(lst)-1]

direction = True

while len(compcards) != 0 and len(mycards) != 0:
	
	playlist = []
	
	if direction:
		firstlst = mycards
		secondlst = compcards 
	else:	
		firstlst = compcards
		secondlst = mycards 
	
	makestep(firstlst,playlist,trumpcard)	
	direction = not answerstep(secondlst,playlist,trumpcard)
	
	cardfromlst(lst,firstlst,6-len(firstlst))
	cardfromlst(lst,secondlst,6-len(secondlst))
	
	printstatus(mycards,compcards,lst)

print('\n------------------------')
printstatus(mycards,compcards,lst)
