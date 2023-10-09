# Introduction
When working with IoT WiFi devices on various locations, it may be handy to bring your own WiFi router. Then, the IoT device WiFi settings are independent of the location and it also makes sure that the WiFi setup of the IoT devices will not be impossible because of things as alternative login procedures (PublicRoam) or unavailable WiFi bands.

Although any out-of-service WiFi router could do the job, it would require transport of an additional device and it is not possible to document universal setup procedures for it, given the many router types on the market. And since most IoT hobbyists own some kind of Raspberry Pi, it is just fun to use that as a WiFi router.

The OpenWrt project for WiFi routers has specific builds for the various RPI types, so this seems to be the go-to solution. It turns out however, that documentation to setup the RPI with this firmware is rather fragmented. This README aims to provide slightly more comprehensive instructions.

Note that the setup described below does not include an internet connection, but only a LAN between the ethernet port and the WiFi access point of the RPI. It is probably possible to define a second radio interface on the RPI and have that connect to the internet via a public WiFi access point, but we leave that as a future exercise.

# RPI as OpenWrt WiFi router

Setting up your RPI as an OpenWrt WiFi router comprises a number of steps, which are described in the sections below. It is assumed that you have a separate computer/laptop with WiFi and an SD-card reader available.

## Step 0:
Update your Raspberry 

## Step 1: SD-card with the OpenWrt image
Download the binary image from the [OpenWrt Raspberry Pi page](https://openwrt.org/toh/raspberry_pi_foundation/raspberry_pi#installation) and be sure to select the right RPI model from the "Firmware OpenWrt Install" column. I used version  22.03.05 for the RPI400.

Various options to flash the image to an SD-card are listed on [that same page](https://openwrt.org/toh/raspberry_pi_foundation/raspberry_pi#installation). Personally, I used the fdisk utility from Ubuntu to first remove all existing partitions from the card and erase all data by formatting a new partition. I did the flashing simply with Ubuntu's "System/Administration/Startup Disk Creator".

## Step 2: Ethernet connection
After booting the RPI with the newly flashed SD-card, connect your computer/laptop back-to-back with the RPI using an ethernet cable (connecting via an ethernet switch is possible too, unless it does not connect to other devices on a different LAN). Now comes the first check: see if your computer/laptop received an IP address from the RPI dhcp service. On Ubuntu, use "ifconfig" or "ip addr" in a terminal and you should have received an IP address on the 192.168.1.0/24 subnet. Using "sudo nmap -nL 192.168.1.0/24" you should also see the RPI itself with an out-of-the-box fixed IP address.

## Step 3: WiFi firmware
The ['Updating the WiFi firmware'](https://openwrt.org/toh/raspberry_pi_foundation/raspberry_pi#updating_the_wifi_firmware) section of the OpenWrt Raspberry Pi page mentions that the WiFi interface does not function optimally without some addditional WiFI firmware files from the linux kernel. My personal experience is that OpenWrt does not recognize the WiFi hardware at all without them.

So, just download and rename the three files listed in the link above and copy them to the connected running OpenWrt system, using scp:

```bash
userx@laptop:~$ scp brcm* root@openwrt:/lib64/firmware/brcm
```

When using a computer/laptop with Microsoft Windows, the three brcm* files can be copied with the [WinSCP file manager](https://winscp.net/eng/index.php).

Alternatively, [this post](https://forum.openwrt.org/t/raspberry-pi-400-no-wireless-file-in-etc-config-directory-and-no-wifi/125275/10) provides download links and commands to get a version of the WiFi firmware out of the Raspbian bullseye distribution (this is what I did for my working setup before reading the supposedly more durable official OpenWrt instructions linked to above).

## Step 4: OpenWrt configuration
Once the right WiFi firmware is in place, OpenWrt does an honourable job in generating /etc/config/network and /etc/network/wireless configuration files. One missing step, however, is the creation of a bridge between the RPI's ethernet and WiFi interfaces. Consequently, WiFi devices cannot connect to the RPI with OpenWrt because the dhcp service linked to the ethernet interface is not visible to them. This is solved by defining a 'br-lan' bridging device and connnecting both interfaces to it, as explained in this [forum post](https://forum.openwrt.org/t/dhcp-not-working-on-wifi/102771).

Although it is possible to configure OpenWrt via its [web interface called LuCI](https://openwrt.org/docs/guide-user/luci/start), the resulting configuration files are not well formatted and hard to compare to example configurations on various internet fora.

Therefore, we rather do a remote login on the OpenWrt system and use the available [vim text editor](https://paulgorman.org/technical/vim5minutes.html) to modify the configuration files:
```
userx@laptop:~$ ssh root@openwrt
root@OpenWrt:~# vim /etc/config/network 
```

When using a computer/laptop with Microsoft Windows, remote configuration changes are even easier with the [WinSCP file manager](https://winscp.net/eng/index.php).

The 'br-lan' device and 'lan' and 'loopback' interfaces are defined in /etc/config/network:
```
config interface 'loopback'
	option device 'lo'
	option proto 'static'
	option ipaddr '127.0.0.1'
	option netmask '255.0.0.0'

config globals 'globals'
	option ula_prefix 'fd15:7708:eaf6::/48'

config device
	option name 'br-lan'
	option type 'bridge'
	list ports 'eth0'
	list ports 'radio0'

config interface 'lan'
	option device 'br-lan'
	option proto 'static'
	option ipaddr '192.168.1.2'
	option gateway '192.168.1.1'
	option dns '192.168.1.1'
	option netmask '255.255.255.0'
	option ip6assign '60'
```

The WiFi device and interface are defined in /etc/config/wireless:
```
config wifi-device 'radio0'
	option type 'mac80211'
	option path 'platform/soc/fe300000.mmcnr/mmc_host/mmc1/mmc1:0001/mmc1:0001:1'
	option channel 'auto'
	option hwmode '11g'

config wifi-iface 'default_radio0'
	option device 'radio0'
	option mode 'ap'
	option ssid 'OpenWrt'
	option network 'lan'
	option key 'secret_wifi_connect_key'
	option encryption 'psk2'
```

Although I did not change any DHCP configurations, I include the /etc/network/dhcp config file of my working setup for completeness. 

```
config dnsmasq
	option domainneeded '1'
	option boguspriv '1'
	option filterwin2k '0'
	option localise_queries '1'
	option rebind_protection '1'
	option rebind_localhost '1'
	option local '/lan/'
	option domain 'lan'
	option expandhosts '1'
	option nonegcache '0'
	option authoritative '1'
	option readethers '1'
	option leasefile '/tmp/dhcp.leases'
	option resolvfile '/tmp/resolv.conf.d/resolv.conf.auto'
	option nonwildcard '1'
	option localservice '1'
	option ednspacket_max '1232'

config dhcp 'lan'
	option interface 'lan'
	option start '100'
	option limit '150'
	option leasetime '12h'
	option dhcpv4 'server'
	option ra 'server'
	option ra_slaac '1'
	list ra_flags 'managed-config'
	list ra_flags 'other-config'

config odhcpd 'odhcpd'
	option maindhcp '0'
	option leasefile '/tmp/hosts/odhcpd'
	option leasetrigger '/usr/sbin/odhcpd-update'
	option loglevel '4'
```

## Step 5: connecting via WiFi
Now come the final checks (and once again, the created OpenWrt LAN does not connect to the internet):

- any WiFi device should now see the OpenWrt SSID and be able to connect with it using the configured key
- the computer/laptop, connected either with the ethernet cable or via WiFi, should be able to see other connected WiFi devices using "sudo nmap -nL 192.168.1.0/24".

If these checks fail, your best option - apart from rechecking all steps made above - is to inspect the system log via the [LuCI web GUI](https://openwrt.org/docs/guide-user/luci/start) and search the internet for any problems that were logged by OpenWrt.



