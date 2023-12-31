# IoT-Guard : Enable Secure Communication and Authentication servies for IoT devices using Blockchain technology
<h6>start the code tracking process from Device.py</h6>
<p>
<h3>Implementation environment</h3>
  
In this section we deal about the usage of laptop
and ESP8266 environment on which we
performed our implementation.<br>
1.Laptop:<br>
The current scheme is implemented on a Windows
11 computer with an Intel 64-bit Core i5 processor
running at 4.5 GHz and 8GB of GDDR6 VRAM,
as well as Python Flask (python3) as the software
configuration. We built one blockchain server,
one cluster header, and one IoT device as part of
our implementation of the entire process.<br>
2.ESP8266:<br>
ESP8266 is a low-cost Wi-Fi microchip with full
TCP/IP stack and microcontroller capabilities,
designed for Internet of Things (IoT) applications.
ESP8266 can be used as a standalone
microcontroller or as a Wi-Fi module for other
microcontrollers, making it a popular choice for
DIY electronics projects. It supports various
communication protocols, such as HTTP, MQTT,
and WebSocket, and can be programmed using the
Arduino IDE or other programming languages
such as MicroPython and Lua. The chip is
available in different variations, such as ESP-01,
ESP-12, and ESP-32, each with different pin
configurations, memory, and features. ESP-01 is
the smallest and cheapest version with limited
GPIO pins, while ESP-32 is a more powerful and
feature-rich variant with dual-core processor,
more GPIO pins, and support for Bluetooth and
BLE.
</p>
<br>
<h3>System Model Description</h3><br>
<p>
  The proposed system consists of two phases, first
is cluster creation and member authentication and
the second is secret key generation and M2M
communication. The clusters are formed based on
the angular distance (AD) in the cluster formation
and member authentication phase, meaning that
the device must first be a certain distance away
from the CH in order to join the cluster and
become a CM. (called cluster radius R). When a
device enters the CH range, it transmits a request
to join the cluster with the device ID (Did). CH
transmits the device its public-key Chpub. The
device joins the cluster once it has obtained the
cluster ID and the public key for CH.
Additionally, the CH generates the block with the
device ID on the blockchain server. During the
secret-key generation and M2M conversation
phases, AES encryption is used to secure M2M
communication. For member to member
communication the device must have the secret
key generated by CH. Initially the M1 sends a
request for communication to M2 M2 sends a
second request to CH verification of M1 and Sk
generation. CH verifies the member’s
identification through the blockchain server if the
member’s block exists, which means the member
is authentic. If not a warning message is generated
by CH to the requesting device. After The verification of M1 , CH generates a one-time secret
key Sk
and sends it to both members. The communicate
using symmetric key encryption. In this system we
used hybrid cryptosystem with blockchain
technology.
</p>

<h3>Description</h3>
<p>
  We use a highly scalable trust
mechanism to build the clusters, allowing devices
to join and exit the cluster more quickly. Every
device must first join the cluster and go through a
safe authentication process before it can
communicate with other cluster devices. To
provide reliable security we used hybrid
cryptography system. ECDSA-based public-key
encryption and decryption is used for
communication between cluster members (CM)
and cluster head (CH). Secret-key cryptography
used for M2M communication, which is an AES
based encryption/decryption method. 
</p>

