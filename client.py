import socket

HOST = "127.0.0.1"
PORT = 5000

# إنشاء socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# الاتصال بالسيرفر
client_socket.connect((HOST, PORT))

# إرسال رسالة
client_socket.send("Bonjour serveur !".encode())

# استقبال الرد
response = client_socket.recv(1024).decode()
print("📩 Réponse du serveur :", response)

client_socket.close()
