# Estudiar sobre Raspberry Pi 4 B

-   Processor: Broadcom BCM2711, quad-core Cortex-A72 (ARM v8) 64-bit
    SoC @ 1.5GHz (Sin multithreading)
-   Memory: 1GB, 2GB, 4GB or 8GB LPDDR4 (depending on model) with on-die
    ECC (La memoria ECC detecta y corrije errores)
-   Connectivity: 2.4 GHz and 5.0 GHz IEEE 802.11b/g/n/ac wireless LAN,
    Bluetooth 5.0, BLE Gigabit Ethernet 2 × USB 3.0 ports 2 × USB 2.0
    ports.
-   GPIO: Standard 40-pin GPIO header (fully backwards-compatible with
    previous boards)
-   Video & sound: 2 × micro HDMI ports (up to 4Kp60 supported) 2-lane
    MIPI DSI display port 2-lane MIPI CSI camera port 4-pole stereo
    audio and composite video port
-   Multimedia: H.265 (4Kp60 decode); H.264 (1080p60 decode, 1080p30 encode);
-   OpenGL ES, 3.0 graphics
-   SD card support: Micro SD card slot for loading operating system and
    data storage
-   Input power: 5V DC via USB-C connector (minimum 3A1 )
-   5V DC via GPIO header (minimum 3A1 )
-   Power over Ethernet (PoE)--enabled (requires separate PoE HAT)
-   Environment: Operating temperature 0--50ºC

<https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-product-brief.pdf>

# Procesador Broadcom BCM2711

-   Processor: Quad-core Cortex-A72 (ARM v8) 64-bit SoC @ 1.5 GHz
-   Memory: Accesses up to 8GB LPDDR4-2400 SDRAM (depending on model)
-   Caches: 32kB data + 48kB instruction L1 cache per core. 1MB L2 cache
-   Multimedia: H.265 (4Kp60 decode); H.264 (1080p60 decode, 1080p30
    encode); OpenGL ES, 3.0 graphics
-   I/O: PCIe bus, onboard Ethernet port, 2 × DSI ports (only one
    exposed on Raspberry Pi 4B), 2 × CSI ports (only one exposed on
    Raspberry Pi 4B), up to 6 × I2C, up to 6 × UART (muxed with I2C), up
    to 6 × SPI (only five exposed on Raspberry Pi 4B), dual HDMI video
    output, composite video output

<https://www.raspberrypi.com/documentation/computers/processors.html>

# GPU

Nombre: VideoCore IV 3D

The main specification points for a fully configured system at 250 MHz
are:

-   25M rendered triangles/s.
-   1G pixels/s with single bilinear texturing, simple shading, 4x
    multisampling.
-   Supports 16x coverage mask antialiasing for 2D rendering at full
    pixel rate.
-   720p standard resolution with 4x multisampling.
-   Supports 16-bit HDR rendering.
-   Fully supports OpenGL-ES 1.1/2.0 and OpenVG 1.1.

<https://docs.broadcom.com/doc/12358545>
