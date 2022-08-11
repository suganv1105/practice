'''
import server
def server_program():
    host=socket.gethostname()
    port=8000
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    conn,address=server_socket.accept()
    while True:
        data=conn.recv(1024).decode()
        if not data:
            break
        print(data)
        message=input("enter your data:")
        conn.send(message.encode())
    conn.close()
if __name__=="main_":
    server_program()
'''

# server.py
import time, socket, sys

print("\nWelcome to Chat Room\n")
print("Initialising....\n")
time.sleep(1)

s = socket.socket()
host = socket.gethostname()
print(host)
ip = socket.gethostbyname(host)
print(ip)
port = 1234
s.bind((host, port))
print(host, "(", ip, ")\n")
name = input(str("Enter your name: "))

s.listen(2)
print("\nWaiting for incoming connections...\n")
conn, addr = s.accept()
print("Received connection from ", addr[0], "(", addr[1], ")\n")

s_name = conn.recv(1024)
s_name = s_name.decode()
print(s_name, "has connected to the chat room\nEnter [e] to exit chat room\n")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        print("\n")
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(s_name, ":", message)