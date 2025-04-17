from scapy.all import *

from generate_mac import generate_mac
import random
import math

import sys

sys.path.insert(1, "C:\\Users\\PC3\\Desktop\\command\\src\\python")

from utils.random_hex import random_hex


def arp_table():

    ipAddr_A = "10.90.90.13"

    macAddr_A = '00:aa:bb:cc:dd:e1'

    ipAddr_B = "10.90.90.1"

    macAddr_B = '00:aa:bb:cc:dd:e0'
    #
    broadcastMacAddr = "ff:ff:ff:ff:ff:ff"

    # req

    pktReq = Ether(src=macAddr_A, dst=broadcastMacAddr) / ARP(
        op=1,
        psrc=ipAddr_A,
        pdst=ipAddr_A,
        hwsrc=macAddr_A,
        hwlen=6,
        plen=4,
        hwdst='00:00:00:00:00:00')

    pktReq.show()

    sendp(pktReq, iface="eth1")

    # res

    pktRes = Ether(src=macAddr_B, dst=broadcastMacAddr) / ARP(
        op=2,
        psrc=ipAddr_B,
        pdst=ipAddr_A,
        hwsrc=macAddr_B,
        hwlen=6,
        plen=4,
        hwdst=broadcastMacAddr)

    pktRes.show()
    ls(ARP)
    sendp(pktRes, iface="eth1")

    # 偷
    packet = ARP(op=2,
                 pdst="10.90.90.16",
                 hwdst="08:00:27:04:18:04",
                 psrc="10.90.90.2")
    send(packet, iface="eth1")


if __name__ == '__main__':

    arp_table()
