import socket

HOST = '' # Enter IP or Hostname of your server
PORT1 = 6677 #Port for defend
PORT2 = 6678 #Port for monitor
socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket1.connect((HOST,PORT1)) #Socket for defend
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2.connect((HOST,PORT2)) #Socket for monitor

#Lets loop awaiting for your input
while True:
	command = raw_input('Enter your command: ')
	socket1.send(command.encode())
	socket2.send(command.encode())
	reply1 = socket1.recv(1024).decode()
	print 'Reply: ' + reply1
	if reply1 == 'Terminate':
		break
	
