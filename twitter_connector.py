import json
import oauth2 


#return clinet - connector to twitter through oauth2
def make_client(): 
	
	# INSERT YOUR ACCESS DATA !! 
	ACCESS_TOKEN = ''
	ACCESS_SECRET = '' 
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''

	consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
	token = oauth2.Token(key=ACCESS_TOKEN, secret=ACCESS_SECRET)
	
	return oauth2.Client(consumer, token)


def query_to_twitter(words,lang='',geo=''):

	url = 'https://api.twitter.com/1.1/search/tweets.json?q={}'.format(words)
	if lang: url += ' lang=%s' %lang 

	client = make_client()
	resp, content = client.request( url, 'GET')
	print('Server answer: {}'.format(resp['status']))
	data = json.loads(content.decode('utf-8'))

	return data


def print_twitts(tw_data):

	colums_to_print = ('user','id_str','text')

	for twitt in tw_data.get('statuses'): 
		print '\n'
		for colum in colums_to_print:
			if colum == 'user': #user - dict, lets print name and id from it
				user_name = str(twitt.get(colum).get('name'))
				user_id = str(twitt.get(colum).get('id_str'))
				print 'user {}  id {}'.format(user_name,user_id)
			else:	
				print '{}: {}'.format(colum,str(twitt.get(colum)))
		

inputed_query = raw_input('Enter search word(s)')

query_data = query_to_twitter(inputed_query) 

print_twitts(query_data)

# with open('twitter_data.txt','w') as data_file:
# 	json.dump(query_data,data_file)
