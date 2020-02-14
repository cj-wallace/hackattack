import socket

HOST = '' # Server IP or Hostname
PORT = 6678 # Open Port For Monitor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#managing error exception
try:
	s.bind((HOST, PORT))
except socket.error as error:
	print 'Bind failed: %s' % error
	quit()


s.listen(0)
print 'Socket listening'

(conn, addr) = s.accept()
print 'Connected at %s' % str(addr)

# awaiting for message
while True:
	data = conn.recv(1024).decode()
	print 'Received: %s' % data
	
	reply = ''
	
	# process your message
	if data == 'hello':
		reply = 'Hi, back!'
	elif data == 'do-task':
		reply = 'OK, I have done the task you have asked me!'
	elif data == 'quit':
		conn.send('Terminate')
		break
	else:
		reply = 'Unknown command'
	
	reply = reply.encode()
	
	conn.send(reply) # Send reply
conn.close() #Close Connection
print 'Closed Connection'
s.close()
print 'Socket Closed'
