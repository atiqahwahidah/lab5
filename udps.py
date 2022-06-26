import socket

localip_addr= "192.168.56.103"
port= 20001
buffer= 1024

msgServer= "Thanks!"
c= str.encode(msgServer)

UDPs_sock= socket.socket(family= socket.AF_INET, type= socket.SOCK_DGRAM)
print ("Socket done.")

UDPs_sock.bind((localip_addr, port))

print("Client is being waited.")

while True:
	bytesAddrPair= UDPs_sock.recvfrom(buffer)
	
	msg= bytesAddrPair
	addr= bytesAddrPair[1]

	clientMsg= "Got connection from: "+ str(addr).format(msg)
	print(clientMsg)

	UDPs_sock.sendto(c, addr)
	buffer= c.recv(1024)
	print(buffer)

	c.close()
