import random

lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

class deck_class():
	
	def __init__(self,list=[]):
		
		self.cards = list
		self.sortlist = []
		self.trumpcard = ''
		
	def define_new_cardslist(self):
		
		for card in lstcards:
			for mast in lstlears: 
				self.cards.append(card+mast)
				
		self.shuffle()
		self.trumpcard = self.cards[-1]
		self.define_sort_list()
	
	def	define_sort_list(self):
	
		lstlears.remove(self.trumpcard[1])
		random.shuffle(lstlears)
		
		for card in lstcards:
			for lear in lstlears: 		
				self.sortlist.append(card+lear)
		
		for card in lstcards:
				self.sortlist.append(card+self.trumpcard[1])	
	
	def shuffle(self):
		random.shuffle(self.cards) 		
			
	def sort_by_list(self,sortlist=[]):
		if not sortlist: sortlist = self.sortlist
		self.cards.sort(key=lambda x: deck.sortlist.index(x)) 
	
	def leght(self):
		return len(self.cards) 
	
	def next_card_fromdeck_to_list(self,lstto,amount):

		amount = min(amount,self.leght()) 
		if amount < 1: 
			return False
		
		lstto.append(self.cards.pop(0))

		if amount > 1:
			self.next_card_fromdeck_to_list(lstto,amount-1) 

		return True

class cards_on_hands_class(deck_class):
	
	def __init__(self):
		self.cards = []
		
	def take_cards_from_deck(self,deck):		
		deck.next_card_fromdeck_to_list(self.cards,6-self.leght())
		self.sort_by_list(deck.sortlist)
	

#defines direction for first step (which card list moves firts)
def definedirection(firsthand,secondhand):

	trumpslst1 = []
	trumpslst2 = [] 

	for card1 in firsthand.cards:
		if card1[1] != deck.trumpcard[1]:
			continue 
		trumpslst1.append(card1)

	for card2 in secondhand.cards:
		if card2[1] != deck.trumpcard[1]:
			continue 
		trumpslst2.append(card2) 

	if len(trumpslst1)==0: return True
	if len(trumpslst2)==0: return False
	trumpslst1.sort(key=lambda x: deck.sortlist.index(x))
	trumpslst2.sort(key=lambda x: deck.sortlist.index(x))

	return deck.sortlist.index(trumpslst1[0]) <  deck.sortlist.index(trumpslst2[0])
	
#move
#if automuve=True: comp make move, 
#if automuve=False:  user makee choice
def makestep(lstfrom,playlist,automove=True): 
	
	if len(lstfrom) == 0:	
		return False 		
	
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
			lstadding.sort(key=lambda x: deck.sortlist.index(x))
			if len(lstadding) != 0:
				card = lstadding[0]	
				if card[1] == deck.trumpcard[1]:
					if deck.leght()/2 > 8-lstcards.index(card[0]): 
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

	hitlist = []
	for card in lstfrom:
		if card[1] == playlist[-1][1]: 
			if lstcards.index(card[0]) > lstcards.index(playlist[-1][0]):
				hitlist.append(card)
		else:
			if playlist[-1][1] != deck.trumpcard[1] and card[1] == deck.trumpcard[1]:
				hitlist.append(card)
	
	if automove:	
		hitlist.sort(key=lambda x: deck.sortlist.index(x))		
		card = ''
		if len(hitlist) > 0: 		
			card = hitlist[0]
			if card[1] == deck.trumpcard[1]:
				if deck.leght()/2 > 9-lstcards.index(card[0]): 
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
		playlist.append(card)
		lstfrom.remove(card)
		return True

def printstatus(mycards,compcards,sometext=''):
	
	print('\n'+sometext)
	print('my - '+str(len(mycards))+' '+str(mycards))
	print('comp - '+str(len(compcards))+' '+str(compcards))
	print('deck - '+str(deck.leght())+' '+str(deck.cards))
		
def printgamestep(mycards,playlist,directon):
	
	if directon:
		sometext = 'Your move '
	else:
		sometext = 'Your answer '

	print('\n'+'Batch '+str(step)+' '+sometext)
	print('cards - '+str(len(mycards))+' '+str(mycards))
	print('playlist - '+str(len(playlist))+' '+str(playlist))
	print('cards left - '+str(deck.leght())+' ; trumpcard - '+str(deck.trumpcard))	
			
print('============================================')
		
deck = deck_class()
deck.define_new_cardslist()

mycards_class = cards_on_hands_class()
mycards_class.take_cards_from_deck(deck)

compcards_class = cards_on_hands_class()
compcards_class.take_cards_from_deck(deck)

direction = definedirection(mycards_class,compcards_class)
step = 0

while compcards_class.cards and mycards_class.cards:
	
	step += 1
	playlist = [] #list of current game session (before pass out)
	
	if direction:
		firstlst = mycards_class.cards
		secondlst = compcards_class.cards 
	else:	
		firstlst = compcards_class.cards
		secondlst = mycards_class.cards 
	
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

	mycards_class.take_cards_from_deck(deck)
	compcards_class.take_cards_from_deck(deck)
	
	print('Batch '+str(step)+' ended.')

if not mycards_class.cards and not compcards_class.cards:
	status = 'CHOICE'	
elif mycards_class.cards and compcards_class.cards:	
	status = 'SOMETHONG WRONG'	
elif mycards_class.cards: 
	status = 'COMP WIN'	
elif compcards_class.cards: 
	status = 'YOU WIN'		

print('\n----------- '+status+' -------------')
printstatus(mycards_class.cards,compcards_class.cards,'left cards:')
