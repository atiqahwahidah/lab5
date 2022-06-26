import socket
import os

ip = "192.168.56.103"
port = 8008
buf_size = 4096
SEP = "<SEPERATE>"
s = socket.socket()
s.bind(('',port))
s.listen(5)
print(f"Listen to {ip}:{port}")
c_s, address = s.accept()
print(f"Connected to {address}")
try:
    filename = c_s.recv(buf_size).decode()
    filesize = c_s.recv(buf_size).decode()
    filename = os.path.basename(filename)
    filesize = int(filesize)
    with open(filename, "wb") as f:
        while True:
            bytes_read = c_s.recv(buf_size)
            if not bytes_read:
                break
            f.write(bytes_read)
except:
    print("ERROR!SERVER IS TERMINATED!")
c_s.close()
s.close()
