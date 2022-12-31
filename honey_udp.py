import socket

target_host = "localhost" 
target_port = 80

# socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send data
client.sendto(b"Hikvision iVMS-4200", (target_host, target_port))

# receive data
data, addr = client.recvfrom(4096)
print(data)

# nc -ulp 80

