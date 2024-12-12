import socket

# Create a UDP socket
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Get the message from the user
message = input("Enter the message and press ENTER to send: ")

# Define the server address and port (127.0.0.1 is localhost)
server_address = ("127.0.0.1", 21)

try:
    # Send the message
    udp_socket.sendto(message.encode(), server_address)
    print("Message sent!")
finally:
    # Close the socket
    udp_socket.close()