#!/usr/bin/python3

import subprocess
import re

#vylepseny skript na hladanie sieti a ich udajov

def scan_wifi():
    try:
        scan_output = subprocess.check_output(['iwlist', 'scanning'], stderr=subprocess.STDOUT).decode('utf-8')
    except subprocess.CalledProcessError as e:
        print("[!] Iwlist neni stiahnuty, musis stiahnut wireless-tools.AK je stiahnuty, spusti skript ako root alebo sudo")
        print(e)
        return
    cells = scan_output.split('Cell ')
    networks = []

    for cell in cells[1:]:
        network = {}

        bssid_match = re.search(r'Address: ([\w:]+)', cell)
        if bssid_match:
            network['BSSID'] = bssid_match.group(1)

        ssid_match = re.search(r'ESSID:"(.*)"', cell)
        if ssid_match:
            network['SSID'] = ssid_match.group(1)
        else:
            network['SSID'] = "<Hidden>"

        freq_match = re.search(r'Frequency:([\d\.]+) GHz', cell)
        if freq_match:
            network['Frequency'] = float(freq_match.group(1))
        else:
            network['Frequency'] = None

        channel_match = re.search(r'Channel:(\d+)', cell)
        if channel_match:
            network['Channel'] = int(channel_match.group(1))
        else:
            channel_alt_match = re.search(r'Frequency:.*\sChannel:(\d+)', cell)
            if channel_alt_match:
                network['Channel'] = int(channel_alt_match.group(1))
            else:
                network['Channel'] = None

        networks.append(network)

    print(f"{'SSID':<30} {'BSSID':<20} {'Frekvencia (GHz)':<10} {'Kanal':<7}")
    print('-' * 70)
    for net in networks:
        print(f"{net['SSID']:<30} {net['BSSID']:<20} {net['Frequency']:<10} {net['Channel']:<7}")

if __name__ == "__main__":
	print("[+] SKenujem...")
	scan_wifi()

