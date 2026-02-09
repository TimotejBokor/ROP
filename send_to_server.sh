#!/bin/bash

read -p "[+] Zadaj Ip adresu na odoslanie: " address
read -p "[+] Zadaj username na server: " usrnam
#ked chces zmenit priecinok na odoslanie, zmen toto
senderdir="/root/home/logger/logs/"

ping -c 1 $address > /dev/null
if [[ $? -ne 0 ]];then
	echo "[!] IP adresa neexistuje!"
	exit 1
else
	echo "[+] Adresa najdena"
fi

#ked chces vytvorit iny logfile, vytvor premennu a pridaj to premennej logfiles
response_file="/root/home/kali/log/logfile.txt"

logfiles="$response_file"

for logfile in $logfiles;do
	if [[ ! -f $response_file ]];then
		echo "[!] Logfile $logfile neexistuje, nemam co poslat"
	else
		echo "[+] Logfile $logfile existuje, idem odoslat"
		scp "$logfile" "address@usrnam:senderdir"
	fi
done
