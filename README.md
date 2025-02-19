# ARP Scanner

A simple ARP scanner written in Python using Scapy to detect devices on a local network.

## Features
- Sends ARP requests to detect active hosts.
- Displays IP and MAC addresses of discovered devices.
- Supports scanning a single IP or an entire subnet.

## Requirements
- Python 3.x
- Scapy library

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/arp-scanner.git
   ```
2. Navigate to the project directory:
   ```sh
   cd arp-scanner
   ```
3. Install dependencies:
   ```sh
   pip install scapy
   ```

## Usage
Run the script with administrator privileges:
```sh
python arp_scanner.py -t 192.168.1.1/24
```

Replace `192.168.1.1/24` with the IP range you want to scan.

## Example Output
```
IP Address        MAC Address
-----------------------------------
192.168.1.2      AA:BB:CC:DD:EE:FF
192.168.1.3      11:22:33:44:55:66
```

## Notes
- This script requires administrative privileges to run properly.
- Ensure you have WinPcap or npcap installed on Windows.

## License
This project is licensed under the MIT License.

