import nmap

scanner = nmap.PortScanner()
ip = "127.0.0.1"

# Adresse IP cible
# 127.0.0.1 correspond à la machine locale (localhost)

scanner.scan(ip, "1-100")

print(f"Résultats du scan pour {ip} :")

for host in scanner.all_hosts():
    print(f"\nHost détecté : {host}")

    for proto in scanner[host].all_protocols():
        print(f"Protocole : {proto}")

        ports = scanner[host][proto].keys()

        for port in ports:
            state = scanner[host][proto][port]['state']
            print(f"Port {port} → {state}")
            # Affichage du numéro du port et de son état

