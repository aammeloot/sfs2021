import socket

remoteServer = input("Enter a remote host")
remoteIP = socket.gethostbyname(remoteServer)

# Go over ports 1 - 1024
try:
    for port in range(1, 1025):

        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Connect to IP/port
        # Warning only one parameter, a tuple
        # Can be misleading 
        result = sock.connect_ex((remoteIP, port))

        if result == 0:
            print("port: ", port, "open")

        sock.close()

except socket.error:
    print("Couldn't connect to the server")
    exit