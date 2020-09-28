import argparse
import socket
import datetime
import random
import sys

MAX_BYTES = 65535
PORT = 1234
HOST = '127.0.0.1'


class Server:
	def __init__(self,host,port):
		self.host = host
		self.port = port

	def  connect(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.bind((self.host, self.port))
		print(" Server is listening at {}". format(sock.getsockname()))

		while True:
			data, address = sock.recvfrom(MAX_BYTES)
			text = data.decode('ascii')
			print('The client at {} say: \n{}'. format(address,text))
			s_text = 'Your data was {} bytes long'. format(len(text))
			s_data = s_text.encode('ascii')
			sock.sendto(s_data, address)


class Client:

	def __init__(self,host,port):
		 self.host = host
		 self.port = port

	def connect(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		sock.connect((self.host, self.port))


		delay = 0.1


		text = 'Welcome!...The time is {}'. format(datetime.datetime.now())
		data = text.encode('ascii')

		now = datetime.datetime.now().time()
		

		while True:
			sock.send(data)
			print('Waiting up to {} seconds for a reply' .format(delay))
			sock.settimeout(delay)

			try:
				reply = sock.recv(MAX_BYTES)
			except socket.timeout:
				if (datetime.time(12,0,0) <= now <= datetime.time(16,59,59)):
					delay *= 2
					if delay > 2:
						raise RuntimeError('Something goes wrong!') 

				elif (datetime(17,0,0) <= now <= datetime.time(23,59,59)):
					delay *= 3
					if delay > 4:
						raise RuntimeError('Something goes wrong!') 


				elif (datetime(0,0,0) <= now <= datetime.time(11,59,59)):
					delay *= 2
					if delay > 1:
						raise RuntimeError('Something goes wrong!') 
			else: break


		text = reply.decode('ascii')
		print("Server send message:{}" . format(text))



def main():
	choices = {"server": Server, "client":Client}
	parser = argparse.ArgumentParser(description = "UDP Client-Server based ")
	parser.add_argument('choice', choices=choices, help='client or server')
	parser.add_argument('-host', metavar="HOST",type=str, help='HOST address ',default=HOST)
	parser.add_argument('-port', metavar='PORT', type=int, help='PORT number: 1234', default=PORT)
	args = parser.parse_args()
	
	#if args.choice == "client":
	#	client = Client(args.host, args.port)
	#	client.connect()
	#elif args.choice == "server":
	#	server = Server(args.host, args.port)
	#	server.connect()

	function = choices[args.choice]
	fun = function(args.host, args.port)
	fun.connect()


if __name__ == '__main__':
	main()