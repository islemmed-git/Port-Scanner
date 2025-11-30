import nmap

scanner = nmap.PortScanner()

ip = "127.0.0.1"
scanner.scan(ip, "1-1024")

print(f"Résultats du scan pour {ip} :")

for host in scanner.all_hosts():
    print(f"\nHost détecté : {host}")

    for proto in scanner[host].all_protocols():
        print(f"Protocole : {proto}")

        ports = scanner[host][proto].keys()

        for port in ports:
            state = scanner[host][proto][port]['state']
            print(f"Port {port} → {state}")
