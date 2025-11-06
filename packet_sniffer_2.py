#!/usr/bin/python3

#importovanie kniznic
import argparse
from scapy.all import *
from os import system

#nastavenie argument cez command line
parser = argparse.ArgumentParser()
parser.add_argument('--interface', help="do tohoto argumentu zadate interface, na ktorom chcete sledovat pakety", required=True)
args = parser.parse_args()

def handle_packet(packet):
	if packet.haslayer(TCP): #tato podmienka kontroluje, ci packet obsahuje TCP vrstvu
		src_ip = packet[IP].src
		dst_ip = packet[IP].dst
		#extrakcia zdrojovej a destinacnej ip adresy
		src_port = packet[TCP].sport
		dst_port = packet[TCP].dport
		#extrakcia zdrojoveho a destinacneho portu

def main(inteface):
	system("clear")
	system("echo -e '\033[1;32m'")
	print("""
		#### #   # # ### ### ### ###
		#    ##  # # #   #   #   #  #
		#### # # # # ### ### ### ###
		   # #  ## # #   #   #   #  #
		#### #   # # #   #   ### #  #
			""")
	pocet = int(input("[+] Zadajte, kolko paketov chcete snimat: "))
	#sniff funkcia, ktora snima tolko paketov, ktore sa urcia v count premennej na urcenom interface, nasledne puzijeme lamba funkciu handle_packet
	paket = sniff(iface=interface, count=pocet, prn=lambda pkt: handle_packet(pkt))
	paket.show()
	system("echo -e '\033[0m'")

interface = args.interface

main(interface)
