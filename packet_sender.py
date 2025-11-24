#!/usr/bin/python3

from os import system
from scapy.all import *

def create_packet():
	type = input("TCP alebo UDP[1/2/3]: ")
	src_mac = input("zadaj zdrovoju mac adresu[d pre originalnu]:  ")
	dst_mac = input("zadaj cielovu mac adresu[d pre originalnu]: ")
	src_addr = input("Zadaj zdrojovu adresu: ")
	dst_addr = input("Zadaj cielovu adresu: ")
	t_t_l = input("zadaj ttl[0/d] pre zakladny]: ")
	if t_t_l == "0" or t_t_l == "d":
		t_t_l = 64

	layer_3 = IP(src=src_addr, dst=dst_addr, ttl=t_t_l)
	layer_2 = Ether(src=src_mac, dst=dst_mac)
	packet = layer_2 / layer_3
	if type == "1" or type == 1:
		s_port = input("zadaj s port: ")
		d_port = input("zadaj d port")
		packet = packet / TCP(sport=s_port, dport=d_port)
	elif type == "2" or type == 2:
		s_port = input("zadaj s port")
		d_port = input("zadaj d port")
		packet = packet / UDP(sport=s_port, dport=d_port)


while True:
	create_choice = input("chces vytvorit paket[y/n]")
	if create_choice == "n" or create_choice == "no":
		system(exit)

	create_packet()
	send_choice = input("chces odoslat paket[y/n]")
	if send_choice == "n" or create_chocie == "no":
		systme(exit)

	send(packet)