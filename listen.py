import socket
import threading

IP = '0.0.0.0'
PORT = 80


dato1 = []
def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(5)
    print(f'[*] Listening traffic to: {IP}:{PORT}')

    
    while True:
        client, address = server.accept()
        print(f'[*] Accepted conection from {address[0]}:{address[1]}')
        dato1.append('{address[0]}:{address[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()
    
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode("utf-8")}')
        sock.send(b'ACK o TCP o lo que sea!!!')

if __name__ == '__main__':
   pd = main()

print(pd)
# print(dato1 + 'holalala')