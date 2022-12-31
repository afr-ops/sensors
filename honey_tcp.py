import socket

target_host = "www.elea.com" #"192.168.0.57" 
target_port = 445


#21 b'220 FTP Server ready.\r\n'
#25 vps vxsct2009.avnam.net GoDaddy.com, LLC
#53 b'' dns
#80 b'HTTP/1.1 400 Bad Request
#110 pop3 b'+OK Dovecot ready.\r\n' 
#143 imap b'* OK Waiting for authentication process to respond..\r\n' 
#443 ssl b''
#445 microsoft-ds 

# socket obj
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# conect client
client.connect((target_host, target_port))

# send data
# client.send(b"GET / HTTP/1.1\r\nHOST:honey_net :)\r\n\r\n")
client.send(b"HUAWEI TECHNOLOGY CO., LT\r\nHOST:honey__ :)\r\n\r\n")

# receive data
respose = client.recv(4096)
print(respose)
# print(respose.decode())
# client.close()
# nc -lvnp