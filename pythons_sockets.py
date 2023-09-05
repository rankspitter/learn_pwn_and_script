# import socket

# # LHOST = '127.0.0.1'
# # LPORT = 42069

# # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # #socket.AF_INET = IPv4
# # #socket.SOCK_STREAM = TCP or UDP


# # s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# # #socket.SOL_SOCKET = Socket level
# # #socket.SO_REUSEADDR = Reuse socket address

# # s.bind((LHOST, LPORT))
# # #Bind the socket to the address and port
# # s.listen(1)
# # #Listen for incoming connections

# # while True:
# #     connect, address = s.accept()
# #     print(f'Connection from {address}')
# #     data = connect.recv(1024)

# #     if not data:
# #         break
# #     else:
# #         print(f'Message to echo: {data}')
    
# #     connect.sendall(data)
# #     connect.close()



# import socket

# RHOST = '127.0.0.1'
# RPORT = 42069

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((RHOST, RPORT))

# msg = "Hello there!".encode()
# #encode() = converts string to bytes
# s.sendall(msg)
# #sendall() = sends all data at once

# data = s.recv(1024)
# #recv() = receives data
# print(data.decode())
# s.close()




