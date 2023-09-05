# from pwn import *

# RHOST = '127.0.0.1'
# RPORT = 42069

# conn = remote(RHOST, RPORT)

# msg = "Hello there!".encode()
# conn.sendline(msg)

# data = conn.recvline()
# print(data.decode())

# conn.close()



# Receiving data

# recv(n) - Receive any number of available bytes
# recvline() - Receive data until a newline is encountered
# recvuntil(delim) - Receive data until a delimiter is found
# recvregex(pattern) - Receive data until a regex pattern is satisfied
# recvrepeat(timeout) - Keep receiving data until a timeout occurs
# clean() - Discard all buffered data
# Sending data

# send(data) - Sends data
# sendline(line) - Sends data plus a newline


# nc <address> <port>
# nc is a utility that allows you to read and write data across network connections, using the TCP or UDP protocol.