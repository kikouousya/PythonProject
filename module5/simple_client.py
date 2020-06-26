import socket
obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
obj.connect((host,8081))

obj.send(input('>>:').encode())

print(obj.recv(1024))


obj.close()