#fin game 
import random

StartCapital = 0
EarnedMoney = 0
SpentMoney = 0

#expample QestionYesNo('Are you ready? ')
def QestionYesNo(mesage):

	print('') 
	answer = raw_input(mesage+'. Y or N ? ') 
	#print('answer - '+answer)
	
	if answer == 'y':
		return True
	elif answer == 'n':
		return False
	else: 
		print('You need to input - "y" or "n" letter. Please try again')
		QestionYesNo(mesage)

#expample QuestionFromArray('Choise variant ','1234')	
def QuestionFromArray(message,inputarray):
	 
	print('\n'+message) 
	
	if isinstance(inputarray,type('')): 
		variantslist = list(inputarray)
		
	elif isinstance(inputarray,type({})): 			
		
		message = ''
		for key in sorted(inputarray.keys()):
			print(key+' - '+inputarray[key])		
		
		variantslist = list(sorted(inputarray.keys()))	
		
	else:
		variantslist = inputarray

	answer = raw_input('Your choise - '+str(variantslist)+'? : ')
	#print('answer - '+answer)
	
	if len(answer) == 1 and answer in variantslist:
		return answer
	else:
		print('You need to input one the variant - '+str(variantslist)+'. Please try again')
		QuestionFromArray(message,variantslist)
		
def printbalance():
	
	if StartCapital != 0:
		profitability = round((EarnedMoney-SpentMoney)/StartCapital,3)
	else:
		profitability = 0
		
	print('---=== Balance ===---' 
	'\nincome: {} , outcome: {} , balance: {} , profitability: {}'.format(EarnedMoney,SpentMoney,EarnedMoney-SpentMoney,profitability))
		
def StringByCondition(ConditionBoolean=False,TextToPrint=''): 
	
	if ConditionBoolean:
		return TextToPrint
	else:	
		return ''	

print('\nLet`s star the business game')

startquestion  = QestionYesNo('Are you ready? ')

if startquestion: 
	print('\nYou in the game')
else:		
	print('\nNo matter. You in the game anyway')	

BusinessTypeChoise = {'1':'Restoran','2':'Closes shop','3':'Car washing','4':'IT company'}
#print('Choose type of business')

BusinessType = QuestionFromArray('Choise business variant ',BusinessTypeChoise)

if BusinessType == '4':
	print('\nGood trying. But you don`t ready for it'
	'\nRandomizer will make appropriate choise for you')
	while BusinessType == '4':
		BusinessType = random.choice(list(BusinessTypeChoise.keys()))
	
	print('You business - %s ' %BusinessTypeChoise[BusinessType])

else:	
	print('%s - good choise' %BusinessTypeChoise[BusinessType])
	
StartCapital = int(raw_input('\nHow much money would you like to invest? '))

while StartCapital < 1000:	
	print('\n%s is not enough. Try again' %StartCapital)
	StartCapital = int(raw_input('How much money would you like to invest? '))

StartMonth1 = QestionYesNo("Start month 1?")
	
print('\n--=== Month 1 start %s===--' %StringByCondition(not StartMonth1,'anyway'))
	
EarnedMoney = round(StartCapital*0.05)

print('\n---------------------'
'\nMonth 1 has passed' 
'\nYou income in month1 is $%s' %EarnedMoney)

printbalance()

StartMonth2 = QestionYesNo("Start month 2?")

print('\n--=== Month 2 start %s===--' %StringByCondition(not StartMonth2,'anyway')) 	
print('\nWhat do you want to do with prices for month 2?')

PricesList = {'1':'Rise prices','2':'Make discount','3':'Left them'}
PricesChoise = QuestionFromArray('Choise prices action ',PricesList)

if PricesChoise == '1':
	
	RisingPercent = int(raw_input('Input percent for rising: '))
	while RisingPercent < 0 or RisingPercent > 100: 
		print('Range for rising must be beetween 0 and 100! Try again')
		RisingPercent = int(raw_input('Input percent for rising'))
	
	EarnedMoney2 = round(StartCapital*0.05*(1-RisingPercent/100))
	
elif PricesChoise == '2':
	
	DiscountPercent = int(raw_input('Input percent for discount: '))
	while DiscountPercent < 0 or DiscountPercent > 100: 
		print('Range for discount must be beetween 0 and 100! Try again')
		DiscountPercent = int(raw_input('Input percent for rising'))
	
	if DiscountPercent > 70: 
		EarnRatio = -0.9*DiscountPercent/100
	elif DiscountPercent > 50: 
		EarnRatio = -0.8*DiscountPercent/100	
	elif DiscountPercent > 30: 
		EarnRatio = 1.05*(1+DiscountPercent/100)
	else:  
		EarnRatio = 1.1*(1+DiscountPercent/100)			
	#print(EarnRatio) 
	EarnedMoney2 = round(StartCapital*0.05*EarnRatio)
	
elif PricesChoise == '3': 	
	EarnedMoney2 = round(StartCapital*0.05)
	
EarnedMoney += EarnedMoney2

print('\n---------------------'
'\n''Month2 has passed' 
'\n''You income in month2 is $%s' %EarnedMoney2)

printbalance()	
	
StartMonth3 = QestionYesNo("Start month 3?")

print('\n--=== Month 3 start %s===--' %StringByCondition(not StartMonth3,'anyway')) 
print('\n''Inspector has came! '
'\n''He wants to close you'
'\n''What are you going to do?')
	
InspectorList = {'1':'Give a bribe','2':'Hit him and get him out','3':'Do nothing'}
InspectorChoise = QuestionFromArray('Choise inspector action ',InspectorList)

PoliceChoise = '0'

if InspectorChoise == '1':
	BribeAmountInspector = int(raw_input('How many do you want to give?'))
	while BribeAmountInspector < round(StartCapital*0.01):
		print('phhhh! Inspector said %s not enough. Give him more!' %BribeAmountInspector)
		BribeAmountInspector = int(raw_input('How many do want to give?')) 
		
	SpentMoney += BribeAmountInspector 

elif InspectorChoise == '2': 	
	print(''
	'\nInspector have called police'
	'\nThey came and ask you what do you supposed to do')
	PoliceList = {'1':'Give a bribe to all of them','2':'Give up to them','3':'Run'}
	PoliceChoise = QuestionFromArray('Choise police action ',PoliceList)
	
	if PoliceChoise == '1':
		BribeAmountPolice = int(raw_input('How many do want to give? '))
		while BribeAmountPolice < round(StartCapital*0.1):
			print('\nPphhhh! Police and inspector said it`s %s not enough. Propose them more!' %BribeAmountPolice)
			BribeAmountPolice = int(raw_input('How many do want to give? ')) 
			
		SpentMoney += BribeAmountPolice	
		
	elif PoliceChoise == '2':	
		PoliceBrideFixedTo2 = round(StartCapital*0.05)
		print('\nYou was fined on $%s for hitting' %PoliceBrideFixedTo2)
		print('And you still have problem with inspector')
		SpentMoney += PoliceBrideFixedTo2 
		
	elif PoliceChoise == '3':	
		PoliceBrideFixedTo3 = round(StartCapital*0.1)
		print('\nGood trying. But you was coght.' 
		'\nAnd fined on $%s for hitting and trying to run' %PoliceBrideFixedTo3)
		print('And you still have problem with inspector')
		
		SpentMoney += PoliceBrideFixedTo3  
		
if InspectorChoise != '1':
	
	print('\nInspector came back on the next day with tax police to clouse you %s business' %BusinessTypeChoise[BusinessType])
	
	if InspectorChoise == '3':
		InspectorBrideTo3 = round(StartCapital*0.1)
	else:
		InspectorBrideTo3 = round(StartCapital*0.15)
	
	print('\nThey want bribe for not clousing - $%s' %InspectorBrideTo3)
	AnswerBribe3 = QestionYesNo('Give them - $%s ?' %InspectorBrideTo3)
	
	if AnswerBribe3: 
		SpentMoney += InspectorBrideTo3
	else: 
		print('\n-- You are arested and your money conficated --')
		SpentMoney = EarnedMoney

printbalance()

print ('Game over')
