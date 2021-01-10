import socket

with socket.socket() as client_socket:
    hostname = '127.0.0.1'
    port = 9090
    address = (hostname, port)
    client_socket.connect(address)
    client_socket.send("message".encode())
    response = client_socket.recv(1024)
    print(response)
