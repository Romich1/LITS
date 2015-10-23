import random
		

def makecardslist():
	
	lst = []	
	for mast in lstlears: 
		for card in lstcards:
			lst.append(mast+card)
	return lst
	
def lstforsorting(trumplear):
	
	lst = []	
	lstlears.remove(trumplear)
	random.shuffle(lstlears)
	
	for card in lstcards:
		for lear in lstlears: 		
			lst.append(lear+card)
	
	for card in lstcards:
			lst.append(trumplear+card)		

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

#move
def makestep(lstfrom,playlist): 
	
	if len(lstfrom) == 0:	
		return False 
		
	lstfrom.sort(key=lambda x: sortinglst.index(x))  
		
	if len(playlist) == 0: # first step:
		card = lstfrom[0]
	else:
		card = random.choice(lstfrom);
		
	playlist.append(card)
	lstfrom.remove(card)			
	
	return True 

#countermove		
def answerstep(lstfrom,playlist):

	if len(lstfrom) == 0 or len(playlist) == 0:
		return False 
		
	hitlist = []
	for card in lstfrom:
		if card[0] == playlist[-1][0]: 
			if lstcards.index(card[1]) > lstcards.index(playlist[-1][1]):
				hitlist.append(card)
		else:
			if playlist[-1][0] != trumpcard[0] and card[0] == trumpcard[0]:
				hitlist.append(card)
		
	hitlist.sort(key=lambda x: sortinglst.index(x))
	print(hitlist)
	
	if len(hitlist) == 0: 
		lstfrom.extend(playlist)
		return False
	 
	playlist.append(hitlist[0])
	lstfrom.remove(hitlist[0])
	
	return True

def printstatus(mycards,compcards,lst,sometext=''):
	
	print('\n'+sometext)
	print('my - '+str(len(mycards))+' '+str(mycards))
	print('comp - '+str(len(compcards))+' '+str(compcards))
	print('lst - '+str(len(lst))+' '+str(lst))
		
			
print('============================================')
		
lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

#lstnew = makecardslist(lstlears,lstcards)
#lst = shufflecards(lstnew) 
lst = makecardslist()
random.shuffle(lst) 
trumpcard = lst[-1]
sortinglst = lstforsorting(trumpcard[0])

mycards = []
compcards = []
cardfromlst(lst,mycards,6-len(mycards))
cardfromlst(lst,compcards,6-len(compcards))
mycards.sort(key=lambda x: sortinglst.index(x))
compcards.sort(key=lambda x: sortinglst.index(x))

direction = True
step = 0

while len(compcards) != 0 and len(mycards) != 0:
	
	playlist = [] #list of current game session (before pass out)
	
	addtext = 'step - '+str(step)+'  direction - ' + str(direction) 
	printstatus(mycards,compcards,lst,addtext)
	
	if direction:
		firstlst = mycards
		secondlst = compcards 
	else:	
		firstlst = compcards
		secondlst = mycards 
	
	makestep(firstlst,playlist)	
	if answerstep(secondlst,playlist):
		direction = not direction

	cardfromlst(lst,firstlst,6-len(firstlst))
	cardfromlst(lst,secondlst,6-len(secondlst))	
	step += 1	

print('\n------------------------')
printstatus(mycards,compcards,lst)
