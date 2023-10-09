"""
Strategy for automatically calibrating tasmota smartplugs:
- manuallyy create one reference smartplug that is calibrated using
  a multimeter and some suitable load of about 500 W. For this we
  use the Athom PG01V2 plug with:
    name in webUI: Athom M1
    hostname on IP network: tasmota-F17F56-8022
    MAC-address: E0:98:06:F1:7F:56
- plug the plug(s) to calibrate into the Athom M1 plug and be sure
  they are all connected to the same local IP network and configured
  for the mjs-voltage MQTT-broker in the cloud
"""
import subprocess




# nmap when both laptop and plug Athom M1 plug are on the hotspot subnet
#sterre@HP:~$ sudo nmap -sn 192.168.43.0/24
#Starting Nmap 7.80 ( https://nmap.org ) at 2023-09-22 19:46 CEST
#Nmap scan report for _gateway (192.168.43.1)
#Host is up (0.13s latency).
#MAC Address: 8E:F5:A3:8F:29:57 (Unknown)
#Nmap scan report for 192.168.43.244
#Host is up (0.037s latency).
#MAC Address: E0:98:06:F1:7F:56 (Unknown)
#Nmap scan report for sterre-HP-Pavilion-TS-15-Notebook-PC (192.168.43.66)
#Host is up.
#Nmap done: 256 IP addresses (3 hosts up) scanned in 8.16 seconds
#sterre@HP:~$ 

# nmap when both laptop and plug Athom M1 plug are on proper WiFi AP subnet
#sterre@HP:~$ sudo nmap -sn 192.168.2.0/24
#[sudo] wachtwoord voor sterre: 
#Starting Nmap 7.80 ( https://nmap.org ) at 2023-09-22 20:18 CEST
#Nmap scan report for fritz.box (192.168.2.1)
#Host is up (0.0026s latency).
#...
#MAC Address: 8C:F5:A3:8F:29:57 (Samsung Electro-mechanics(thailand))
#Nmap scan report for tasmota-F17F56-8022.fritz.box (192.168.2.71)
#Host is up (0.12s latency).
#MAC Address: E0:98:06:F1:7F:56 (Unknown)
#Nmap scan report for sterre-HP-Pavilion-TS-15-Notebook-PC.fritz.box (192.168.2.42)
#Host is up.
#Nmap done: 256 IP addresses (11 hosts up) scanned in 3.93 seconds
#sterre@HP:~$ 


