# Tasmota for smart plugs

The Tasmota software can run on many smart plugs with the ESP8266 microcontroller. Using Tasmota in a project where smart plugs connect to a cloud MQTT broker gives rise to two issues:

1. Standard Tasmota images do not include secure MQTT using TLS. For this, the Tasmota image needs to be built with the MQTT-TLS feature.
2. Many smart plugs come with a proprietary image and need to be reflashed with the Tasmota software. One could still want to buy such plugs because of the nicer form factor (e.g. Gosund vs Athom).

## Tasmota with secure MQTT
Instructions for building a custom image and "over the air" upgrading:

- [https://tasmota.github.io/docs/TLS/](https://tasmota.github.io/docs/TLS/)
- [https://tasmota.github.io/docs/Upgrading/](https://tasmota.github.io/docs/Upgrading/)

## Flashing plugs without tasmota

- [https://tasmota.github.io/docs/Tuya-Convert/](https://tasmota.github.io/docs/Tuya-Convert/)
- [https://github.com/tasmota/tasmotizer](https://github.com/tasmota/tasmotizer)
- [https://github.com/arendst/Tasmota/discussions/10350](https://github.com/arendst/Tasmota/discussions/10350)
- [https://sylvainzimmer.com/blog/2021/09/smart-plugs-tasmota/](https://sylvainzimmer.com/blog/2021/09/smart-plugs-tasmota/)
- [https://www.sbprojects.net/projects/sonoff/](https://www.sbprojects.net/projects/sonoff/)
- [https://github.com/ct-Open-Source/tuya-convert/issues/483](https://github.com/ct-Open-Source/tuya-convert/issues/483)

## Smart plugs in use
- Done: Compile tasmota including MQTT TLS
- Done: Find better programmer (mod or rebuy) USB-TTL-programmers based on an 2102 chip do not supply sufficient current to the ESP8285! Need programmer with CH340 chip, e.g. [https://www.bol.com/nl/nl/p/otronic-ch340-ttl-usb-serial-port-adapter-3-3v-5v-hw-597](https://www.bol.com/nl/nl/p/otronic-ch340-ttl-usb-serial-port-adapter-3-3v-5v-hw-597) These are available at the Hahaho Makey Mondays.

After upgrading or flashing, the plugs do not have the right configs anymore. Profiles below can be configured via the plug's web UI.

Athom v2 plugs (after upgrading to tasmota-12.5.0 with MQTT TLS)
[https://templates.blakadder.com/athom_PG01V2-EU16A-TAS.html](https://templates.blakadder.com/athom_PG01V2-EU16A-TAS.html)
{"NAME":"Athom Plug V2","GPIO":[0,0,0,3104,0,32,0,0,224,576,0,0,0,0],"FLAG":0,"BASE":18}

Gosund EP2 plugs (after flashing with Tasmota)
[https://templates.blakadder.com/gosund_EP2.html](https://templates.blakadder.com/gosund_EP2.html)
{"NAME":"Gosund EP2","GPIO":[576,1,320,1,2656,2720,0,0,2624,32,0,224,0,0],"FLAG":0,"BASE":45}


## Tasmota WiFi behaviour
Although the configuration menu in the Tasmota web UI offers an option to enter alternative values for the ssid and password, the firmware does not seem to try and use these alternative values when the primary values fail. This might be a bug (tested on v 12.5.0 on the Athom v2 and Gosund EP2 plugs). Possibly, the secondary access point settings rather apply to a second Wifi module that can be connected to an ESP32 chip (not for ESP8266).

The behaviour described above implies that a Tasmota smart plug can only be connected to a different WiFi network than initially configured, by [device recovery](https://tasmota.github.io/docs/Device-Recovery/). However, device recovery is painful because all settings are reset to firmware defaults (including calibration).

A temporary workaround is to change the [WifiConfig](https://tasmota.github.io/docs/Commands/#wi-fi) from the default *4 = retry other AP without rebooting* to *2 = set Wi-Fi Manager as the current configuration tool*. If the device cannot connect to the Wifi using the primary access point settings, the [WifiManager](https://github.com/tzapu/WiFiManager/blob/master/README.md#how-it-works) is run for 3 minutes during which the smart plug functions as a Wifi access point and runs a web UI on the 192.168.4.1 IP address. There, it is possible to configure new values for the ssid and password.

One can apply this workaround manually by entering the following commands in the console of the smart plug's web UI:

- `WebPassword my_secret_password` &nbsp;&nbsp; [if not already done via the web UI]
- `WifiConfig 2`
- `Restart 1`

Although the custom Tasmota build allows the WifiManager to be set as a firmware default, this is not recommended because it implies a serious safety issue: if the primary WiFi is unavailable, anyone in the neighbourhood of the plug can detect it functioning as an access point without WPA2 security. The username/password protection is run by - assumably - vulnerable software. Also, the password can be read in case of physical access to the plug.


## Upgrading Tasmota firmware on Athom v2 plugs
Original Tasmota version: 10.1.0 (device M1) and 13.0.0 (device M2)
Custom built version: 12.5.0 with MQTT-TLS

Standard firmware versions are to be found at [http://ota.tasmota.com/tasmota/release-12.5.0/](http://ota.tasmota.com/tasmota/release-12.5.0/)

To sidestep storage limitations of the ESP8266, the upgrade must be performed in two steps from the device's web UI:

1 Upgrade from the web to ota.tasmota.com/tasmota/release-12.5.0/tasmota-minimal.bin.gz
2 Upgrade by uploading the custom build 12.5.0 firmware with MQTT-TLS (tasmota.bin.gz)


Interesting: https://www.amazon.de/dp/B0054PSIPA?ref=myi_title_dp&th=1


