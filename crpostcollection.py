import requests
import random
url = "https://www.postman.com/collections/"
randchar = "0123456789abcdef"
def random_char(y):
       return ''.join(random.choice(randchar) for x in range(y))
while True:
	rand_hash = random_char(20)
	print(rand_hash)
	rep = requests.get(url+rand_hash)
	print(rep.text)
