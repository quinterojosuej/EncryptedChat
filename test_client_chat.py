# Python program to implement client side of chat room. 
import socket 
import select 
import sys 
import math
import encrypt_header
import time
import json
from PyQt5.QtCore import QThread

key = 0;
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
name="Richard"#input("please enter your username:")
"""tmp = input("enter IP address")
sys.append(tmp)
tmp = input("enter port number")
sys.append(tmp)"""
sys.argv.append('127.0.0.1')#"192.168.43.101")
sys.argv.append(25565)
if len(sys.argv) != 3: 
	print ("Correct usage: script, IP address, port number")
	exit() 
IP_address = str(sys.argv[1]) 
Port = int(sys.argv[2]) 
server.connect((IP_address, Port))
self_ob = encrypt_header.client(name,(IP_address,Port))


#intial handshake
"""
message = "";
while (message!="accept"):
	#recived result
	message = server.recv(2048)
	message.decode("utf-8")

	if message =="accept":
		break;

	#send password
	tmp_password = input("enter password")
	tmp_password.encode()
	server.send(tmp_password)
	pass
"""
#end intial handshake

#handshake
message = server.recv(2048)
message = message.decode("utf-8")
if("time_seed:" == message[0:10]):
	x = [int(s) for s in message.split() if s.isdigit()]
	tmp_seed = x[0]
	print(tmp_seed)
	key = self_ob.key_gen(tmp_seed)
	print("key:",key)
	pub = self_ob.diff_hullman_ex_gen(key)
	server.send(str(key).encode())
	print("Welcome to this chatroom!") 
server.send(name.encode())
"""s_addr = server.recv(2048)
s_addr.decode('utf-8')
self_addr = """

#end handshake

def con_2_person(name):
	server.send(("name:"+name).encode())
	print("line 63")
	message = server.recv(2048)
	print("message:",message)
	tmp_key = int(message.decode("utf-8"))
	return tmp_key

		
def send_message(message,name):
	tmp_mess= str(self_ob.thread_encrypt(message,key))		
	tmp = json.dumps({"name" : name , "message": tmp_mess})
	#print(self_ob.thread_decrypt(tmp_mess.decode("utf-8"),key),"decoded")
	server.send(tmp.encode()) 
	print("<You>"+message)
	#time.sleep(1)  
	pass


"""class sample(QThread):
	def __init__(self,window,de_key,k):
		super(sample, self).__init__()
		self.window = window
		self.de_key = de_key
	
	def run(self):
		self.listen(self.window,self.de_key,0)
		pass"""

def listen(window,de_key,k):
	print("I'm listening")
	sockets_list = [sys.stdin, server] 
	read_sockets = sockets_list
	print("line 80")
	while True:
		message = server.recv(2048) #problem line
		message = message.decode("utf-8")
		message_json_parse = json.loads(message)
		print("working...",message_json_parse['message'])
		message = self_ob.thread_decrypt(message_json_parse['message'],de_key)
		print("dedcoded:",message)
		if (message!='\0'):
			window.update(message)
			print(("<>")+message)
		else:
			2+2

"""
while True: 
	# maintains a list of possible input streams 
	sockets_list = [sys.stdin, server] 
	read_sockets = sockets_list
	for socks in read_sockets: 
		if socks == server:
			try:
				message = socks.recv(2048) #problem line
				message = message.decode("utf-8")
				if (message!='\0'):
					print(("<>")+message)
				else:
					2+2		
			except:
				print("IP") 
		else:
			message = sys.stdin.readline() 
			tmp_mess= str(self_ob.thread_encrypt(message,key)).encode()		
			tmp_mes = tmp_mess.decode("utf-8")
			print(self_ob.thread_decrypt(tmp_mess.decode("utf-8"),key),"decoded")
			server.send(tmp_mess) 
			print("<You>"+message)
			time.sleep(1)  
"""
def close():
	print("closing")
	server.close() 



"""
Time log 
RHL - 3/14/19 5pm - 7:30pm (2hrs 30min)
RHL - 3/17/19 3:00- 3:47pm (47min)
RHL - 3/18/19 10am - 12:00am (1hr 42 min)
RHL - 3/18/19 12:37pm - 1:30pm (1hr)
RHL - 3/18/19 7-8pm (1hr)
RHL - 3/19/19 6-7:30pm (1hr 30 min)
RHL - 3/20/19 4-6:41pm (2hr 41min)
RHL - 3/24/19 4-6:10(2hr 10 min)
RHL - 3/26/19 9:45 -11:40pm(1hr 55min)
RHL - 3/28/19 10:45 - 12:00
RHL - 3/28/19 7:30 - 
15hr 15min total
"""
