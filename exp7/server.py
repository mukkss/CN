import socket


def main():
    host = '127.0.0.1'  # localhost
    port = 4000

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print("Server ready for connection")

        conn, addr = server_socket.accept()
        with conn:
            print("Connection is successful and waiting for chatting")
            # Receiving the filename from the client
            filename = conn.recv(1024).decode()

            try:
                with open(filename, 'r') as file:
                    # Sending each line of the file to the client
                    for line in file:
                        conn.sendall(line.encode())
                    print("Contents of the file have been sent...")
            except FileNotFoundError:
                print(f"File '{filename}' not found.")
                conn.sendall(b"File not found.")


if __name__ == "__main__":
    main()