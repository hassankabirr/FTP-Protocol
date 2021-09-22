from socket import *
import os
import pickle
import random
serverPort = 2122
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("127.0.0.1", serverPort))

serverSocket.listen(10)
print("server is ready")
print("listening ......")
while True:
    connectionSocket, addr = serverSocket.accept()
    cmd = connectionSocket.recv(1024).decode()
    if cmd == "hi":
        connectionSocket.send("***Help***\nhelp ......... show list of command\nlist ......... list of file and dir \npwd ......... current path in server \n"
                              "dwld <filename> ......... download file to clinet\ncd ......... to move in dir".encode())
    elif cmd == "help":
        connectionSocket.send("***Help***\nhelp ......... show list of command\nlist ......... list of file and dir \npwd ......... current path in server \n"
                              "dwld <filename> ......... download file to clinet\ncd ......... to move in dir".encode())
    elif cmd[0] == 'c' and cmd[1] == 'd':
        print("cd command request")
        a, b = cmd.split(" ", 1)
        os.chdir(b)
    elif cmd == "pwd":
        print("pwd command request")
        connectionSocket.send(os.getcwd().encode())
    elif cmd == "list":
        print("list command request")
        d = []
        f = []
        for (dirpath, dirnames, filenames) in os.walk(os.getcwd()):
            d.extend(dirnames)
            f.extend(filenames)
            break

        data = pickle.dumps(d)
        connectionSocket.send(data)

        del data
        msg_confirm = connectionSocket.recv(1024)

        data_file = pickle.dumps(f)
        connectionSocket.send(data_file)
        connectionSocket.send(os.getcwd().encode())


    elif cmd[0]=='d' and cmd[1]=='w'and cmd[2]=='l'and cmd[3]=='d':
        print("dwld command request")
        command, dwld_filename = cmd.split(' ', 1)
        port_dwld = random.randrange(3000, 50000)
        socket_dwld = socket(AF_INET, SOCK_STREAM)
        socket_dwld.bind(("127.0.0.1", port_dwld))
        connectionSocket.send(str(port_dwld).encode())
        socket_dwld.listen(5)
        while(True):
            connectionSocket_dwld, addr_dwld = socket_dwld.accept()
            confirm_msg = connectionSocket_dwld.recv(1024).decode()
            file = open(dwld_filename, "rb")
            sending_data = file.read()
            file.close()
            connectionSocket_dwld.send(sending_data)
            confirm_msg2 = connectionSocket_dwld.recv(1024)
            connectionSocket_dwld.close()
            socket_dwld.close()
            break
            print("close")
    connectionSocket.close()


