#!/usr/bin/env python
import scapy.all as scapy
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target", help="Specify target IP or IP range")
    options = parser.parse_args()
    return options


# Function to perform network scan
def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  # Create an ARP request packet for the given IP
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")  # Create an Ethernet frame to broadcast
    arp_req_brd = broadcast / arp_request  # Combine Ethernet frame with ARP request

    # Send the packet and capture the responses
    answered_list = scapy.srp(arp_req_brd, timeout=1, verbose=False)[0]

    clients_list = []  # List to store detected clients
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}  # Extract IP and MAC
        clients_list.append(client_dict)
    return clients_list


# Function to display the scan results
def printer(result_lists):
    print("IP Address\t\tMAC Address\n-----------------------------------")
    for client in result_lists:
        print(client["ip"] + "\t\t" + client["mac"])


opts = get_args()
scan_list = scan(opts.target)
printer(scan_list)  # Execute the scanner and display results
