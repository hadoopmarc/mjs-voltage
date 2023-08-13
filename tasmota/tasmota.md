# Tasmota for smart plugs

The Tasmota software can run on many smart plugs with the ESP8266 microcontroller. Using Tasmota in a project where smart plugs connect to a cloud MQTT broker gives rise to two issues:

1. Standard Tasmota images do not include secure MQTT using TLS. For this, the Tasmota image needs to be upgraded.
2. Many smart plugs come with a proprietary image and need to be reflashed with the Tasmota software. One could still want to buy such plugs because of the nicer form factor (e.g. Gosund vs Athom).

## Tasmota with secure MQTT
Various instructions for flashing:

- [https://tasmota.github.io/docs/Upgrading/](https://tasmota.github.io/docs/Upgrading/)
- [https://tasmota.github.io/docs/TLS/](https://tasmota.github.io/docs/TLS/)

## Flashing plugs without tasmota

- [https://tasmota.github.io/docs/Tuya-Convert/](https://tasmota.github.io/docs/Tuya-Convert/)
- [https://github.com/tasmota/tasmotizer](https://github.com/tasmota/tasmotizer)
- [https://github.com/arendst/Tasmota/discussions/10350](https://github.com/arendst/Tasmota/discussions/10350)
- [https://sylvainzimmer.com/blog/2021/09/smart-plugs-tasmota/](https://sylvainzimmer.com/blog/2021/09/smart-plugs-tasmota/)
- [https://www.sbprojects.net/projects/sonoff/](https://www.sbprojects.net/projects/sonoff/)
- [https://github.com/ct-Open-Source/tuya-convert/issues/483](https://github.com/ct-Open-Source/tuya-convert/issues/483)

## ToDo:
- Find Gosund versions and check upgradebility (Gosund1: v1.0.?, Gosund2: v1.0.4 X)
- Done: Find better programmer (mod or rebuy) USB-TTL-programmers based on an 2102 chip do not supply sufficient current to the ESP8285! Need programmer with CH340 chip, e.g. [https://www.bol.com/nl/nl/p/otronic-ch340-ttl-usb-serial-port-adapter-3-3v-5v-hw-597](https://www.bol.com/nl/nl/p/otronic-ch340-ttl-usb-serial-port-adapter-3-3v-5v-hw-597) These are available at the Hahaho Makey Mondays.
- Done: Compile tasmota including MQTT TLS
- Done: Upgrade Athom plugs

## Custom Tasmota build with MQTT-TLS



## Upgrading Tasmota firmware on Athom v2 plugs
Original Tasmota version: 10.1.0 (device M1) and 13.0.0 (device M2)
Custom built version: 12.5.0 with MQTT-TLS

Standard firmware versions are to be found at [http://ota.tasmota.com/tasmota/release-12.5.0/](http://ota.tasmota.com/tasmota/release-12.5.0/)

To sidestep storage limitations of the ESP8266, the upgrade must be performed in two steps from the device's web UI:

1 Upgrade from the web to ota.tasmota.com/tasmota/release-12.5.0/tasmota-minimal.bin.gz
2 Upgrade by uploading the custom build 12.5.0 firmware with MQTT-TLS (tasmota.bin.gz)





