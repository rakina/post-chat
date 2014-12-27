import requests
import json
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

def load_chats(last):
	payload = {'last': last}
	r = requests.post("http://chat.rakina.me/getHistory", data=payload, headers=headers)
	newchat = r.json()
	ret = last
	for i in range(len(newchat)):
		print "~ "+newchat[i]['user'] +": " + newchat[i]['message']
		ret = newchat[i]['id']
	return ret

username = raw_input("username: ")
payload = {'username': username}
r = requests.post("http://chat.rakina.me/hello", data=payload, headers=headers)
if (r.status_code != 200):
	exit()

last = r.text
print "enter a blank line to refresh chat"

while (True):
	last = load_chats(last)
	message = raw_input(username+": ")
	print "\033[A                             \033[A" 
	if (message == ""):
		continue
	payload = {'username': username, 'message': message}
	r = requests.post("http://chat.rakina.me/sendMessage", data=payload, headers=headers)
	last = load_chats(last)
	last = r.text