# Tasmota custom build

The Tasmota software can run on [many smart plugs with the ESP8266 microcontroller](https://templates.blakadder.com/plug.html). However, using Tasmota in a project where smart plugs connect to a cloud MQTT broker, gives rise to the issue that standard Tasmota images do not include secure MQTT using TLS. Since smart plug power measurements are somewhat sensitive (e.g. at what times are people at home), it is not advised to use Tasmota without the MQTT-TLS feature enabled. TLS provides end-to-end encryption between the plug and the cloud broker, so that anyone that would intercept IP packets cannot read them.


Obtaining a Tasmota firmaware image with the MQTT-TLS feature requires a custom build. Instructions for doing this can be found at [https://tasmota.github.io/docs/TLS/#compiling-tls-for-esp8266](https://tasmota.github.io/docs/TLS/#compiling-tls-for-esp8266/). This resource provides many options for compiling the software. For the current project, the compilation was done on an old laptop with Ubuntu 20.04 using [the PlatformIO-core option](https://tasmota.github.io/docs/Create-your-own-Firmware-Build-without-IDE/) from Tasmota itself. This is the most basic option that gives good insight in missing dependencies on your system. Running the build on this system for version 12.5.0 took 2.5 hours. The files controlling the custom build are provided at [tasmota/platformio_override.ini](../../tasmota/platformio_override.ini) and [tasmota/user_config_override.h](../../tasmota/user_config_override.h).


Configuring smart plugs with the resulting custom firmware is described [elsewhere](../../doc/deploy/plug-config.md) in this documentation.
