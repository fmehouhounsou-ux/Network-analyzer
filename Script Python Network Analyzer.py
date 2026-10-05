# Données simulées représentant les appareils du réseau
appareils = [
    {"ip": "192.168.1.10", "statut": "Actif", "port": 22},
    {"ip": "192.168.1.15", "statut": "Inactif", "port": 80},
    {"ip": "192.168.1.20", "statut": "Actif", "port": 443},
    {"ip": "192.168.1.10", "statut": "Actif", "port": 22},
    {"ip": "192.168.1.25", "statut": "Inactif", "port": 21}
]


def ips_uniques(appareils):
    """Extrait la liste des adresses IP uniques."""
    ips = []
    for appareil in appareils:
        if appareil["ip"] not in ips:
            ips.append(appareil["ip"])
    return ips


def compter_port(appareils):
    """Extrait la liste des ports distincts utilisés."""
    ports = []
    for appareil in appareils:
        if appareil["port"] not in ports:
            ports.append(appareil["port"])
    return ports


def total(appareils):
    """Retourne le nombre total d'entrées appareils."""
    return len(appareils)


def total_actif(appareils):
    """Comptabilise le nombre d'appareils avec un statut Actif."""
    compteur = 0
    for appareil in appareils:
        if appareil["statut"] == "Actif":
            compteur += 1
    return compteur


def appareils_ssh(appareils):
    """Identifie les adresses IP configurées avec SSH (port 22)."""
    ssh = []
    for appareil in appareils:
        if appareil["port"] == 22 and appareil["ip"] not in ssh:
            ssh.append(appareil["ip"])
    return ssh


def ssh_actifs(appareils):
    """Identifie les adresses IP actives utilisant le protocole SSH."""
    ssh = []
    for appareil in appareils:
        if appareil["port"] == 22 and appareil["ip"] not in ssh and appareil["statut"] == "Actif":
            ssh.append(appareil["ip"])
    return ssh


def ports_sensibles(appareils):
    """Détecte l'utilisation de ports sensibles à risque."""
    ports_a_risque = [21, 22, 23, 3389]
    po = {}
    for appareil in appareils:
        if appareil["port"] in ports_a_risque and appareil["ip"] not in po:
            po[appareil["ip"]] = appareil["port"]
    return po


def analyser_reseau(appareils):
    """Génère le rapport global d'analyse du réseau."""
    nombre_total = total(appareils)
    nombre_actif = total_actif(appareils)
    ips = ips_uniques(appareils)
    ports = compter_port(appareils)
    ssh = ssh_actifs(appareils)
    sensibles = ports_sensibles(appareils)

    print("===== RAPPORT RÉSEAU =====")
    print(f"Nombre total d'appareils : {nombre_total}")
    print(f"Appareils actifs : {nombre_actif}")
    print(f"IPs uniques : {len(ips)}")
    print(f"Ports utilisés : {len(ports)}")
    print(f"Appareils actifs avec SSH : {len(ssh)}")

    print("\n===== PORTS SENSIBLES =====")
    for ip, port in sensibles.items():
        print(f"{ip} → Port {port}")
    print("===========================")


if __name__ == "__main__":
    analyser_reseau(appareils)