import socket


def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_adress = ("127.0.01", 5501)
    server_socket.bind(server_adress)

    print(f"UDP Server is up and listening on {server_adress[0]}:{server_adress[1]}")

    while True:
        data, address = server_socket.recvfrom(4096)
        print(f"Recieved message: {data.decode()} from {address}")

        print(f"write to {address}")
        response = input()
        server_socket.sendto(response.encode(), address)


if __name__ == "__main__":
    udp_server()
