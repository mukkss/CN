import socket

def main():
    host = '127.0.0.1'  # Server's IP address
    port = 4000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))

        # Sending the filename to the server
        filename = input("Enter the file name: ")
        client_socket.sendall(filename.encode())

        # Receiving and displaying the contents of the file from the server
        print("Contents of the File:")
        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            print(data, end="")

if __name__ == "__main__":
    main()