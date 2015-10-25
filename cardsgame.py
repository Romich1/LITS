import random

	
def makecardslist():
	
	lst = []	
	for card in lstcards:
		for mast in lstlears: 
			lst.append(card+mast)
	return lst

#makes full cards list and sort it by value	
def lstforsorting(trumplear):
	
	lst = []	
	lstlears.remove(trumplear)
	random.shuffle(lstlears)
	
	for card in lstcards:
		for lear in lstlears: 		
			lst.append(card+lear)
	
	for card in lstcards:
			lst.append(card+trumplear)		

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

#defines direction for first step (which card list moves firts)
def definedirection(lst1,lst2):

	trumpslst1 = []
	trumpslst2 = [] 

	for card1 in lst1:
		if card1[1] != trumpcard[1]:
			continue 
		trumpslst1.append(card1)

	for card2 in lst2:
		if card2[1] != trumpcard[1]:
			continue 
		trumpslst2.append(card2) 

	if len(trumpslst1)==0: return True
	if len(trumpslst2)==0: return False
	trumpslst1.sort(key=lambda x: sortinglst.index(x))
	trumpslst2.sort(key=lambda x: sortinglst.index(x))

	return sortinglst.index(trumpslst1[0]) <  sortinglst.index(trumpslst2[0])
	
#move
#if automuve=True: comp make move, 
#if automuve=False:  user makee choice
def makestep(lstfrom,playlist,automove=True): 
	
	if len(lstfrom) == 0:	
		return False 
		
	lstfrom.sort(key=lambda x: sortinglst.index(x))  
	
	if automove:
		card = ''	
	else: 
		printgamestep(lstfrom,playlist,True)
		card = input('input card or 0 for pass: ')
		if card == '0' and len(playlist) > 0: return False

	if len(playlist) == 0: # first step:
		
		if automove:
			
			#searching pairs firstly, prioritize firsts cards pair
			if len(lstfrom) > 8 and lstfrom[3][0] == lstfrom[4][0]:
				card = lstfrom[3] 	
			if len(lstfrom) > 6 and lstfrom[2][0] == lstfrom[3][0]:
				card = lstfrom[2] 	
			if len(lstfrom) > 2 and lstfrom[1][0] == lstfrom[2][0]:
				card = lstfrom[1] 	

			if card=='': 
				card = lstfrom[0]
		else:
			if not card in lstfrom: 
				print('You have to choice correct card. Try again') 
				return makestep(lstfrom,playlist,False)	
	
	else:
		
		lstadding = []
		for playcard in playlist:
			for lstcard in lstfrom:
				if lstcard[0] == playcard[0]:
					lstadding.append(lstcard)
		
		if automove:
			lstadding.sort(key=lambda x: sortinglst.index(x))
			if len(lstadding) != 0:
				card = lstadding[0]	
				if card[1] == trumpcard[1]:
					if len(lst)/2 > 8-lstcards.index(card[0]): 
						card = ''				
		else:
			if not card in lstadding: 
				print('You have to choice correct card. Try again') 
				return makestep(lstfrom,playlist,False)		
		
	if card == '':
		return False
	else:			
		playlist.append(card)
		lstfrom.remove(card)			
		return True 	
		
#countermove	
#if cardtochek is not empty - cheking can it be used or not	
def answerstep(lstfrom,playlist,automove=True):

	if len(lstfrom) == 0 or len(playlist) == 0:
		return False 
	
	lstfrom.sort(key=lambda x: sortinglst.index(x)) 

	hitlist = []
	for card in lstfrom:
		if card[1] == playlist[-1][1]: 
			if lstcards.index(card[0]) > lstcards.index(playlist[-1][0]):
				hitlist.append(card)
		else:
			if playlist[-1][1] != trumpcard[1] and card[1] == trumpcard[1]:
				hitlist.append(card)
	
	if automove:	
		hitlist.sort(key=lambda x: sortinglst.index(x))		
		card = ''
		if len(hitlist) > 0: 		
			card = hitlist[0]
			if card[1] == trumpcard[1]:
				if len(lst)/2 > 9-lstcards.index(card[0]): 
						card = ''

	else:
		printgamestep(lstfrom,playlist,False)
		card = input('input card or 0 for taking playlist: ')
		if card != '0' and not card in hitlist: 	
			print('You have to choice correct card. Try again') 
			return answerstep(lstfrom,playlist,False)
		
	if card == '' or card == '0':
		lstfrom.extend(playlist)
		return False 
	else:
		playlist.append(hitlist[0])
		lstfrom.remove(hitlist[0])
		return True

def printstatus(mycards,compcards,lst,sometext=''):
	
	print('\n'+sometext)
	print('my - '+str(len(mycards))+' '+str(mycards))
	print('comp - '+str(len(compcards))+' '+str(compcards))
	print('lst - '+str(len(lst))+' '+str(lst))
		
def printgamestep(mycards,playlist,directon):
	
	if directon:
		sometext = 'Your move '
	else:
		sometext = 'Your answer '

	print('\n'+'Batch '+str(step)+' '+sometext)
	print('cards - '+str(len(mycards))+' '+str(mycards))
	print('playlist - '+str(len(playlist))+' '+str(playlist))
	print('cards left - '+str(len(lst))+' ; trumpcard - '+str(trumpcard))	
			
print('============================================')
		
lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

lst = makecardslist()
random.shuffle(lst) 
trumpcard = lst[-1]
sortinglst = lstforsorting(trumpcard[1])

mycards = []
compcards = []
cardfromlst(lst,mycards,6-len(mycards))
cardfromlst(lst,compcards,6-len(compcards))
mycards.sort(key=lambda x: sortinglst.index(x))
compcards.sort(key=lambda x: sortinglst.index(x))

direction = definedirection(mycards,compcards)
step = 0

while len(compcards) != 0 and len(mycards) != 0:
	
	step += 1
	playlist = [] #list of current game session (before pass out)
	
	if direction:
		firstlst = mycards
		secondlst = compcards 
	else:	
		firstlst = compcards
		secondlst = mycards 
	
	game = True
	while game: 		
		if makestep(firstlst,playlist, not direction): 
			if answerstep(secondlst,playlist, direction):
				game = True
			else:	
				game = False
		else:	
			game = False	
			direction = not direction

	cardfromlst(lst,firstlst,6-len(firstlst))
	cardfromlst(lst,secondlst,6-len(secondlst))	
	print('Batch '+str(step)+' ended.')

if len(mycards) == 0 and len(compcards) == 0:
	status = 'CHOICE'	
elif len(mycards) > 0: 
	status = 'COMP WIN'	
elif len(compcards) > 0: 
	status = 'YOU WIN'		

print('\n----------- '+status+' -------------')
printstatus(mycards,compcards,lst,'left cards:')

