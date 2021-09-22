from socket import *
import pickle
import os

# serverName = "127.0.0.1"
# severPort = 2121
# clientSocket = socket(AF_INET, SOCK_STREAM)
# clientSocket.connect((serverName, severPort))
# clientSocket.send("hi".encode())
# sentence = clientSocket.recv(1024)
# print(sentence.decode())
#
# clientSocket.close()



i = 0
while True:
    server_Name = "127.0.0.1"
    sever_Port = 2122
    client_Socket = socket(AF_INET, SOCK_STREAM)
    client_Socket.connect((server_Name, sever_Port))
    if i == 0:
        com = "hi"
    else:
        com = input("Entet your command : ")

    if com == "end":
        break
    client_Socket.send(com.encode())
    if com == "list":
        list_dir = client_Socket.recv(1024)
        data = pickle.loads(list_dir)
        for x in data:
            print(" > ", x)
        client_Socket.send("confirm".encode())
        list_file = client_Socket.recv(1024)
        data_file = pickle.loads(list_file)
        filesizes = 0
        size_path = client_Socket.recv(1024).decode()
        for y in data_file:
            print("   ", y)
            x = size_path + "\\" +y
            filesizes = filesizes + os.path.getsize(x)
        print(" size of files : ", filesizes)

    elif com[0]=='d' and com[1]=='w'and com[2]=='l'and com[3]=='d':

        dwld_com, dwld_filenaem = com.split(" ", 1)
        port_recive = int(client_Socket.recv(1024).decode())
        dwld_server = "127.0.0.1"
        dwld_socket = socket(AF_INET, SOCK_STREAM)
        dwld_socket.connect((dwld_server,  port_recive))
        dwld_socket.send("connected".encode())
        dwld_data = dwld_socket.recv(2097152)
        file = open(dwld_filenaem, 'wb')
        file.write(dwld_data)
        file.close()
        dwld_socket.send("succssefuly".encode())




    else:
        sentence = client_Socket.recv(2048)
        print(sentence.decode())
        sentence = ''

    i = i+1









