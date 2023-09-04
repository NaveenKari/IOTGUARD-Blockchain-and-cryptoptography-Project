import socket

# Get the hostname of the device
hostname = socket.gethostname()

# Get the IP address of the device
ip_address = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("IP address:", ip_address)
