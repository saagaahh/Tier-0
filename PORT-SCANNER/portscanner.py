import socket
 
target = "127.0.0.1"
 
print(f"Scanning {target}...")
 
for port in range(1, 1025):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "unknown"
        print(f"Port {port} is OPEN ({service})")
    s.close()
 
print("Scan complete.")
