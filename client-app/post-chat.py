import requests
import json

def load_chats(last):
	payload = {'last': last}
	r = requests.post("http://localhost/post-chat/public/getHistory", data=payload)
	newchat = r.json()
	ret = last
	for i in range(len(newchat)):
		print "~ "+newchat[i]['user'] +": " + newchat[i]['message']
		ret = newchat[i]['id']
	return ret

username = raw_input("username: ")
payload = {'username': username}

r = requests.post("http://localhost/post-chat/public/", data=payload)

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
	r = requests.post("http://localhost/post-chat/public/sendMessage", data=payload)
	last = load_chats(last)
	last = r.text