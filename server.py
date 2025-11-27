import socket

HOST = "127.0.0.1"   
PORT = 5000         

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen()

print(" Serveur en attente de connexion...")

connection, address = server_socket.accept()
print("✅ Client connecté :", address)


message = connection.recv(1024).decode()
print("📩 Message reçu du client :", message)
connection.send("Message reçu ✔️".encode())

connection.close()
