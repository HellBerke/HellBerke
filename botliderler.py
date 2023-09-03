import socket
import threading
import openai
import random
import time
import requests
import scapy.all as scapy

openai.api_key = "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"

# Rastgele lider isimleri oluşturmak için liste
leader_names = ["LizzardFree", "WizardOrder", "ST40L", "Sequence", "RedTeamer", "RedHacker", "Anonymer", "AnonWizard", "TrackHunter", "BlueTeamer", "EtterAper", "Rho", "Tau", "Nu", "Mu", "Sy3roX", "Iota", "ScarletT", "Chi", "???"]

class DefenseBot:
    def __init__(self, name, port, ip_address=None):
        self.name = name
        self.ip_address = ip_address if ip_address is not None else self.get_external_ip()
        self.port = port

    def random_ip(self):
        return f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"

    def get_external_ip(self):
        try:
            response = requests.get('https://api64.ipify.org?format=json')
            data = response.json()
            return data['ip']
        except Exception as e:
            print("Dış IP adresi alınırken bir hata oluştu:", str(e))
            return None

    def defense_mission(self):
        self.running_ids = IntrusionDetectionSystem(self.ip_address)
        self.running_ids.start_scanning()
        self.check_data_security()
        self.perform_network_security()

    def check_data_security(self):
        print(f"{self.name} ({self.ip_address}) - Veri güvenliği kontrol ediliyor.")

    def perform_network_security(self):
        self.start_communication_server()
        
        while True:
            time.sleep(1)
            packet = self.monitor_network_traffic()
            detected_attacks = self.running_ids.detect_threat(packet)

            for attack_type in detected_attacks:
                if attack_type == "DDoS":
                    self.ddos_protection(packet)
                elif attack_type == "Hack":
                    self.hack_prevention(packet)
                elif attack_type == "Exploit":
                    self.exploit_prevention(packet)

            if "education" in packet.lower():
                self.educational_module()

            self.communicate_with_other_bots(detected_attacks)

    def monitor_network_traffic(self):
        packet = "GET /index.html HTTP/1.1\r\n"
        packet += "Host: 192.168.1.1\r\n"
        packet += "User-Agent: FWQX | ST40L\r\n"
        packet += "Accept: text/html\r\n\r\n"

        return packet

    def ddos_protection(self, packet):
        pass

    def hack_prevention(self, packet):
        if "ddos" in packet.lower():
            target_ip = self.random_ip()
            self.penetration_test(target_ip)

    def penetration_test(self, target_ip):
        open_ports = []
        start_port = 1
        end_port = 1024

        print(f"{self.name} ({self.ip_address}) - Penetrasyon testi başlatılıyor hedef: {target_ip}")

        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)

            result = sock.connect_ex((target_ip, port))

            if result == 0:
                open_ports.append(port)
                print(f"{self.name} ({self.ip_address}) - Açık port tespit edildi: {port}")

            sock.close()

        if open_ports:
            print(f"{self.name} ({self.ip_address}) - Penetrasyon testi tamamlandı. Açık portlar: {open_ports}")
        else:
            print(f"{self.name} ({self.ip_address}) - Herhangi bir açık port tespit edilmedi.")

    def exploit_prevention(self, packet):
        pass

    def educational_module(self):
        prompt = "Ağ güvenliği hakkında bilgi almak istiyorum."
        response = self.generate_openai_response(prompt)

        print(f"{self.name} ({self.ip_address}) - Eğitim Modülü: Ağ güvenliği hakkında bilgi edinin.")
        print(response)

    def generate_openai_response(self, prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=prompt,
                max_tokens=1
            )
            return response.choices[0].text
        except Exception as e:
            print("OpenAI'den yanıt oluşturulurken bir hata oluştu:", str(e))
            return "Eğitim içeriği oluşturulurken bir hata oluştu."

    def start_communication_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", self.port))
        self.server_socket.listen(5)

        print(f"{self.name} ({self.ip_address}) - İletişim sunucusu dinleniyor ({self.port})")

        while True:
            client_socket, client_address = self.server_socket.accept()
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        data = client_socket.recv(1024)
        message = data.decode("utf-8")
        print(f"{self.name} ({self.ip_address}) - İletişim aldı: {message}")

    def send_message(self, target_ip, target_port, message):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((target_ip, target_port))
        client_socket.send(message.encode("utf-8"))
        client_socket.close()

    def communicate_with_other_bots(self, detected_attacks):
        if detected_attacks:
            for attack_source in detected_attacks:
                # Saldırı kaynağına karşı saldırı başlat
                self.launch_counter_attack(attack_source)

    def launch_counter_attack(self, attack_source):
        print(f"{self.name} ({self.ip_address}) - {attack_source} saldırı kaynağına karşı saldırı başlatılıyor.")

class IntrusionDetectionSystem:
    def __init__(self, bot_ip):
        self.bot_ip = bot_ip
        self.tarama_durumu = False

    def start_scanning(self):
        self.tarama_durumu = True
        print(f"IDS ({self.bot_ip}) - Tarama başlatıldı.")

    def stop_scanning(self):
        self.tarama_durumu = False
        print(f"IDS ({self.bot_ip}) - Tarama durduruldu.")

    def detect_threat(self, packet):
        detected_attacks = []

        if self.tarama_durumu:
            if "DDoS" in packet:
                detected_attacks.append("DDoS")
            if "Hack" in packet:
                detected_attacks.append("Hack")
            if "Exploit" in packet:
                detected_attacks.append("Exploit")

            if detected_attacks:
                print(f"IDS ({self.bot_ip}) - Potansiyel tehditler algılandı:", detected_attacks)

# 20 lider oluşturun
leaders = []
for i in range(20):
    leader_name = random.choice(leader_names)
    leader_port = 5000 + i  # Her liderin port numarasını artırın
    leader = DefenseBot(f"FWQX | {leader_name}", leader_port)
    leaders.append(leader)
    leader.defense_mission()

# Savunma botları arasında iletişim örneği
while True:
    for leader in leaders:
        target_leader = random.choice(leaders)
        if target_leader != leader:
            leader.send_message(target_leader.ip_address, target_leader.port, f"Merhaba, {target_leader.name}!")
    time.sleep(10)  # 10 saniyede bir ileti gönder
