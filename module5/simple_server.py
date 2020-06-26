import socket
obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# obj.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
host = socket.gethostname()
print(host)
obj.bind((host,8083))

obj.listen(5)
conn, addr = obj.accept()
print(conn,'\n',addr)

content = conn.recv(1024)
print(content)
conn.send(content.upper())

