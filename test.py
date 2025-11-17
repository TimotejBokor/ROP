#!/usr/bin/python3

from os import system
import socket

def scan_ports(host, start_port, end_port):
    open_ports = []
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
        	system("echo -e '\033[1;32m'")
        	print(f"[+]Port {port} je otvoreny")
        	open_ports.append(port)
        else:
        	system("echo -e '\033[1;31m'")
        	print(f"[-] Port {port} uzavrety")
        sock.close()

    return open_ports

def scan_port():
	host = input("[+] Zadaj ip adresu: ")
	port = int(input("[+] Zadaj port na skenovanie: "))
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.settimeout(1)
	result = sock.connect_ex((host, port))
	if result == 0:
		system("echo -e '\033[1;32m'")
		print("[+] Port", port, "Otvoreny")
	else:
        	system("echo -e '\033[1;31m'")
        	print("[-] Port", port, "uzavrety")
	sock.close()
	return port

if __name__ == "__main__":
	print("""
		 [1] Porty v rozshahu
		 [2] Specificky port
		 [3] Specificke porty

	""")
	choice = input("[+] Zadaj moznost: ")
	if choice == "1":
		target_host = input("Zadaj ip adresu na skenovanie: ")
		start_port = int(input("prvy port: "))
		end_port = int(input("posledny port: "))

		print(f"Skenujem porty od {start_port} do {end_port} na {target_host}...")
		open_ports = scan_ports(target_host, start_port, end_port)
		if open_ports:
			print("Open ports:", open_ports)
		else:
			print("No open ports found in the specified range.")
	elif choice == "2":
		scan_port()

system("echo -e '\033[0m'")
