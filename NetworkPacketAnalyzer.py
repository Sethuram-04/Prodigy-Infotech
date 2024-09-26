from scapy.all import sniff, IP, Raw
import socket

# Resolve the IP address of www.w3schools.com
w3schools_ip = socket.gethostbyname('www.w3schools.com')

# List to store captured packets
captured_packets = []

# Callback function to process each packet
def packet_callback(packet):
    if packet.haslayer(IP):
        ip_layer = packet[IP]
        # Filter traffic to/from w3schools.com
        if ip_layer.src == w3schools_ip or ip_layer.dst == w3schools_ip:
            captured_packets.append(packet)  # Store the packet
            print(f"Source IP: {ip_layer.src}")
            print(f"Destination IP: {ip_layer.dst}")
            print(f"Protocol: {ip_layer.proto}")
            if packet.haslayer(Raw):
                payload = packet[Raw].load
                print(f"Payload: {payload[:50]}...")  # Show the first 50 bytes of the payload for readability
            print("----------")

def start_sniffer():
    print(f"Starting packet capture for traffic to/from w3schools.com ({w3schools_ip}). Press Ctrl+C to stop.")
    # Apply filter to capture only w3schools traffic and avoid broadcast/multicast traffic
    filter_rule = f"host {w3schools_ip} and not broadcast and not multicast"
    sniff(prn=packet_callback, store=0, filter=filter_rule)

if __name__ == "__main__":
    try:
        start_sniffer()
    except KeyboardInterrupt:
        print("Packet capture stopped. Displaying summary of captured packets:")
        # Output a summary of the captured packets
        for pkt in captured_packets:
            print(pkt.summary())
