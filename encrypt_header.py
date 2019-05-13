import math
from _thread import *
import time
class client:
	"""docstring for client"""
	def __init__(self,s1,address):
		super(client, self).__init__()
		self.name = s1
		self.ip = address[0]
		self.port = address[1]

	def key_gen(self,tmp_seed2):
		#print("before")
		y = int(math.sin(tmp_seed2*tmp_seed2)*10000)
		#y2 = int(math.cos(tmp_seed2*tmp_seed2)*5000)
		#print("after")
		if(y<0):
			y = y*-1;
		return int(y)
	#private = message+public
	#Const = gen(private)

	def diff_hullman_ex_sent(self,a,nb):
		return (nb**a)%2147483647

	def diff_hullman_ex_gen(self,a):
		n = 2305843009213693951;
		return ((n**a)%2147483647)

	def thread_encrypt(self,message2,key):
		print(message2)
		tmp = int(len(message2)/4)
		rmd = len(message2)%4
		place =0
		if tmp ==1:
			tmp = tmp+1
		message_parts = [None]*(tmp-1)
		#print("working")	
		for x in range(tmp-1):#minus one to add on last bit together
			#print(x,tmp)
			#print("pass",place/4)
			if x==tmp-2:
				start_new_thread(self.encrypt,(message2[place:],key,message_parts,place/4))
				#print(message2[place:],"first")
			else:
				start_new_thread(self.encrypt,(message2[place:(place+4)],key,message_parts,place/4))
				#print(message2[place:(place+4)],"first")
			#print(message_parts)
			#print("line 38")
			place=place+4
		#for x in range(tmp):
			#r_message= r_message+message_parts[x]
		print(len(message_parts),tmp,"line 44")
		while not (message_parts[tmp-2]):
			print(message_parts,tmp)
			time.sleep(1)
			pass
		blank = ""
		#print("working")
		print(message_parts)
		for x in range(len(message_parts)):#when you enter a small message the probelm is that the tmp = 2 so for loop no go
			if isinstance(message_parts[x], str):
				blank = blank+message_parts[x]			
			#print(blank,"hi")
			pass
		print(blank)
		return blank

	def thread_decrypt(self,message2,key):
		print(message2,"this is message")
		tmp = int(len(message2)/4)
		rmd = len(message2)%4
		if tmp == 1:
			tmp = tmp+1;
			pass
		message_parts = [None]*(tmp-1)
		print("tmp",tmp)
		place =0
		for x in range(tmp-1):#minus 1 to concatinate last bit of message
			#print(x,tmp)
			if x==tmp-2:
				start_new_thread(self.decrypt,(message2[place:],key,message_parts,place/4))
			else:
				start_new_thread(self.decrypt,(message2[place:(place+4)],key,message_parts,place/4))
				#print(message2[place:(place+4)])#beta remove
			place=place+4
		#print("pass",x)
		print(len(message_parts),tmp)
		while not(message_parts[tmp-2]):
			pass
		blank = ""
		for x in range(len(message_parts)):
			if message_parts[x]==None:
				2+2
			else:
				blank = blank+message_parts[x]
			pass
		return blank
				

	def encrypt(self,message2,key,message_parts,pos):
		message = message2
		message_nums =[]
		for j in range(len(message)):
			message_nums.append(ord(message[j]))
		# 	print(ord(message[j]))
		# print("!")
		for i in range(key):
			#print(message_nums,message2)
			for j in range(len(message)):
				if(j <len(message)-1):
					#print(message_nums[j],"+",message_nums[j+1],"=",message_nums[j]+message_nums[j+1])
					message_nums[j+1] = (message_nums[j]+message_nums[j+1]);
				else:
					#print(message_nums[j],"+",message_nums[0],"=",message_nums[j]+message_nums[0])
					message_nums[0] = (message_nums[j]+message_nums[0]);
			#print(message_nums,message2)
		message = ""
		for tmp in range(len(message2)):
			message_nums[tmp] = message_nums[tmp]%55296
			message = message + chr(message_nums[tmp])
			#print(message_parts,len(message_parts))
		print(message)
		message_parts[int(pos)] = message
		#print("new",message_parts)
		#return tmp_string


	def decrypt(self,message2,key,message_parts,pos):
		message = message2
		message_nums =[]
		for j in range(len(message)):
			try:
				message_nums.append(ord(message[j]))
			except:
				continue
		tmp_length = len(message)-1
		for i in range(key,0,-1):
			#print(message_nums)
			for j in range(tmp_length,-1,-1):
				if(j<tmp_length):
					#print(message_nums[j],"-",message_nums[j+1],"=",message_nums[j]-message_nums[j+1])
					message_nums[j+1] = (message_nums[j+1]-message_nums[j]);
				else:
					message_nums[0] = (message_nums[0]-message_nums[j]);
			#print(message_nums)
		message = ""#sorry senpi
		for tmp in range(tmp_length+1):
		 	message_nums[tmp] = message_nums[tmp]%55296
		 	message = message + chr(message_nums[tmp])
		#print(message2,"adding",message_nums)
		message_parts[int(pos)] = message
		#print("new:  ",message_parts)

