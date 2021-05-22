#!/usr/bin/env python

import scapy.all as scapy

def scan(ip) :
    scapy.arping(ip)

for i in range (0,255):
    x = "1.1.1." + str(i)
    scan(x)
