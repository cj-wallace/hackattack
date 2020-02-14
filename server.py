import socket
import thread

BUFF = 1024
HOST = socket.gethostname()  # Server IP or Hostname
PORT = 6677  # Open Port, must match the client port
score = 0


def handle_thread(conn, addr):
    # Waiting for message
    while True:
        try:
            data = conn.recv(BUFF).decode()
            print addr[1], 'Received: %s' % data

            reply = ''
            # process your message
            if data == 'hello':
                reply = 'Hi, back!'
            elif data == 'do-task':
                reply = 'OK, I have done the task you have asked me!'
            elif data == 'quit':
                conn.send('Terminate')
                break
            elif data == 'up':
                global score
                score += 1
                reply = 'score up: ' + str(score)
            elif data == 'down':
                global score
                score -= 1
                reply = 'score down: ' + str(score)
            else:
                reply = 'Unknown command'

            reply = reply.encode()

            conn.send(reply)  # Send reply
        except Exception as e:
            print e
            print addr[1], 'Client disconnected'
            break
    conn.close()  # Close Connection
    print addr[1], 'Closed Connection'


# Start server
print 'Start Server'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
print 'Socket created'

# Managing error exception
try:
    s.bind((HOST, PORT))
except socket.error as error:
    print 'Bind failed: %s' % error
    quit()

s.listen(5)
print 'Socket listening at', (HOST, PORT)
while True:
    (conn, addr) = s.accept()
    print 'Connected at %s' % str(addr)
    thread.start_new_thread(handle_thread, (conn, addr))
s.close()
print 'Socket Closed'
