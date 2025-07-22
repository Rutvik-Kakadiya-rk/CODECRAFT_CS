from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        ip_layer = packet[IP]
        src = ip_layer.src
        dst = ip_layer.dst
        proto = ip_layer.proto

        protocol = {
            1: 'ICMP',
            6: 'TCP',
            17: 'UDP'
        }.get(proto, 'Other')

        print(f"[+] {protocol} Packet: {src} --> {dst}")

        if packet.haslayer(TCP):
            print(f"    [TCP] Payload: {bytes(packet[TCP].payload)}")
        elif packet.haslayer(UDP):
            print(f"    [UDP] Payload: {bytes(packet[UDP].payload)}")
        elif packet.haslayer(ICMP):
            print("    [ICMP] Packet")
        print("-" * 50)

def main():
    print("📡 Starting Network Packet Analyzer...")
    sniff(prn=analyze_packet, store=False)

if __name__ == "__main__":
    main()
