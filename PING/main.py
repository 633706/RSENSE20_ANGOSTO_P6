from network import LoRa
import socket
import time
import pycom

pycom.heartbeat(False)
colors = [0x003f00,0x3f3f00,0x3f0000]
lora = LoRa(mode=LoRa.LORA, region=LoRa.EU868)
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
s.setblocking(False)
i = 0
while True:
    s.send('Ping')
    print('Ping {}'.format(i))
    i= i+1
    pycom.rgbled(colors[i%len(colors)])
    time.sleep(1)
