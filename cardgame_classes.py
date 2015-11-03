import random


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
		
		for card in lstcards:
			for lear in lstlears: 		
				if lear == self.trumpcard[1]: continue 
				self.sortlist.append(card+lear)
		
		for card in lstcards:
				self.sortlist.append(card+self.trumpcard[1])	
	
	def shuffle(self):
		random.shuffle(self.cards) 		
			
	def sort_by_list(self):
		
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
		

class cards_list(list):
	
	def __init__(self,leght=6):
		self.listleght = leght
		
	def take_cards_from_deck(self,deck):		
		deck.next_card_fromdeck_to_list(self,self.listleght-len(self))
		self.sort_by_list(deck.sortlist)
	
	def sort_by_list(self,sortlist):		
		self.sort(key=lambda x: sortlist.index(x)) 
	
	def make_move_list(self,cards_playlist,trump):
		
		return_list = []
		for playcard in cards_playlist:
			for lstcard in self:
				if lstcard[0] == playcard[0]:
					return_list.append(lstcard)
		
		return return_list
		
	def make_hit_list(self,cards_playlist,trump):
		
		return_list = []
		for card in self:
			if card[1] == cards_playlist[-1][1]: 
				if lstcards.index(card[0]) > lstcards.index(cards_playlist[-1][0]):
					return_list.append(card)
			else:
				if cards_playlist[-1][1] != trump[1] and card[1] == trump[1]:
					return_list.append(card)
		
		return return_list
		
		
#defines direction for first step (which card list moves firts)
def definedirection(cards_list_first,cards_list_second):

	trumpslst1 = []
	trumpslst2 = [] 

	for card1 in cards_list_first:
		if card1[1] != deck.trumpcard[1]:
			continue 
		trumpslst1.append(card1)

	for card2 in cards_list_second:
		if card2[1] != deck.trumpcard[1]:
			continue 
		trumpslst2.append(card2) 

	if not trumpslst2: return True
	if not trumpslst1: return False
	
	trumpslst1.sort(key=lambda x: deck.sortlist.index(x))
	trumpslst2.sort(key=lambda x: deck.sortlist.index(x))

	return deck.sortlist.index(trumpslst1[0]) <  deck.sortlist.index(trumpslst2[0])
	
	
#move
#if automove=True: comp make move automatically 
#if automove=False:  user make interactive choice
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
		
		lstadding = lstfrom.make_move_list(playlist,deck.trumpcard)
		
		if automove:
			lstadding.sort(key=lambda x: deck.sortlist.index(x))
			if len(lstadding) != 0:
				card = lstadding[0]	
				if card[1] == deck.trumpcard[1]:
					if deck.leght()/2 > 8-lstcards.index(card[0]):  #not use big trumps while deck is big
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
	
	
#answerstep
#if automove=True: comp make move automatically 
#if automove=False:  user make interactive choice	
def answerstep(lstfrom,playlist,automove=True):

	if len(lstfrom) == 0 or len(playlist) == 0:
		return False 

	hitlist = lstfrom.make_hit_list(playlist,deck.trumpcard)
	
	if automove:	
		hitlist.sort(key=lambda x: deck.sortlist.index(x))		
		card = ''
		if len(hitlist) > 0: 		
			card = hitlist[0]
			if card[1] == deck.trumpcard[1]:
				if deck.leght()/2 > 9-lstcards.index(card[0]): #not use big trumps while deck is big
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


### GAMPLAY  mthrfckr! ###
def gameplay(mycards,compcards):
	global step 
	
	print('================GAME START================')
	
	direction = definedirection(mycards,compcards) #true - first list makes first move
	
	while mycards and compcards:
	
		step += 1
		playlist = [] #list of current game session (before pass out)
		
		if direction: #first list makes move, second list makes answer 
			firstlst = mycards
			secondlst = compcards 
		else:	
			firstlst = compcards
			secondlst = mycards 
		
		game_session = True #status of continuing current session
		while game_session: 		
			if makestep(firstlst,playlist, not direction): #success move, so continue
				if answerstep(secondlst,playlist, direction): #success answer, so continue
					game_session = True
				else: #answer doesn`t made, so stop session without direction changing
					game_session = False
			else: #move doesn`t made, so change direction and stop session
				game_session = False	
				direction = not direction 

		mycards.take_cards_from_deck(deck)
		compcards.take_cards_from_deck(deck)
		
		print('Batch '+str(step)+' ended.')

				
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
			

def define_result(mycards,compcards):

	if not mycards and not compcards:
		status = 'CHOICE'	
	elif mycards and compcards:	
		status = 'SOMETHONG WRONG'	
	elif mycards: 
		status = 'COMP WIN'	
	elif compcards: 
		status = 'YOU WIN'		

	print('\n----------- '+status+' -------------')
	printstatus(mycards,compcards,'left cards:')	
	print('================GAME END================')


lstlears = ['h','d','c','s']
lstcards = ['6','7','8','9','0','j','q','k','a']

deck = deck_class()
deck.define_new_cardslist()

mycards = cards_list()
mycards.take_cards_from_deck(deck)

compcards = cards_list()
compcards.take_cards_from_deck(deck)

step = 0
gameplay(mycards,compcards)

define_result(mycards,compcards)
