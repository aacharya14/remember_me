from datetime import date


# example: ([Date("02-01-2022"), "I kept my glasses on the desk."])
memory_map = list()

def nice_answer(answer_tuple):
	date = answer_tuple[0]
	phrase = answer_tuple[1]
	return f'On {date} you said "{phrase}".'

def answer_question(question):
	similarity_map = {}
	for idx in range(len(memory_map)):
		date = memory_map[idx][0]
		memory = memory_map[idx][1]
		similarity=0
		for word in question.split():
			if word in memory.split():
				similarity+=1
		similarity_map[idx] = similarity

		#return top 3 results
	print('Here is what I found from your memories:\n')
	similarity_map = list(sorted(similarity_map.items(), key=lambda item: item[1],reverse=True))
	print(nice_answer(memory_map[similarity_map[0][0]]))

def store_response(response):
	today = date.today()
	memory_map.append(tuple([today, response]))

def prompt():
	return input("Tell me something! (Type 'bye' to exit.) If you want to ask me something, make sure your question ends with a question mark.\n").lower()



response = prompt()
while (response != "bye"):
	if '?' in response:
		if len(memory_map) > 0:
			print("I'm thinking...\n")
			answer_question(response.strip('?'))
		else:
			print("I don't know anything yet!\n")
	else:
		print("Thanks, I'll remember that!\n")
		store_response(response)
	response = prompt()



''' NOTES

high-level:
store map of memories: <Date, phrase>
do keyword search

iterations:
- identify key words in a sentence, use those as keys in a map so indexing is faster
- demote old content once replaced (if another instance of where glasses are kept is added)
- build flask app

'''
