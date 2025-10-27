#!/usr/bin/python3

import os
import time
import socket
import struct
import requests
import pandas as pd
import matplotlib.pyplot as plt
from scapy.all import *
from datetime import datetime
from scapy.layers.inet import IP
from sklearn.ensemble import IsolationForest


def ip_to_int(str_ip):
	pass
	#funkcia zoberie danu ip adresu a rozbali ju pomocou struct rozbali a prevedie na integer na lepsie spracovanie

def detect_anomalies(data, contamination_rate):
	pass
	#funkcia podla dat a "miery" kontaminacie deteguje anomalie

def report_anomalies(dataframe):
	pass
	#tato funkcia nahlasi anomalie

def log_anomalies(dataframe):
	pass
	#tato funkcia bude logovat anomalie

#mozna funkcia check_ip_reputation(): pomocou doveryhodneho zdroja zisti reputaciu a legitimitu ip adresy

def sniff_network():
	pass
	#tato funckcia bude sledovat pakety na sieti

def punish():
	#tato funkcia "potresta" utocnika