import socket

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to port 21
try:
    udp_socket.bind(('', 21))  # '' means it listens on all network interfaces
except PermissionError:
    print("Permission denied. Try using a port above 1024 (e.g., 9876).")
    exit(1)

print("Waiting for a message from the server...")

# Receive data from the server
buffer_size = 1024  # Buffer size for incoming messages
data, server_address = udp_socket.recvfrom(buffer_size)

# Decode and print the received message
message = data.decode('utf-8')  # Decode bytes to string
print("Message from Server:")
print(message)

# Close the socket
udp_socket.close()