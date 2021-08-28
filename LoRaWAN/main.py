from network import LoRa
import socket
import time
import ubinascii


lora = LoRa(mode=LoRa.LORAWAN, region=LoRa.EU868)

app_eui = ubinascii.unhexlify('DADADADADADADADA')
app_key = ubinascii.unhexlify('B215C617C28C2569ED2B8AE43D33D146')

lora.init(mode=LoRa.LORAWAN, adr=True, public=True,region=LoRa.EU868)
lora.join(activation=LoRa.OTAA, auth=(app_eui, app_key), timeout=0)
while not lora.has_joined():
    time.sleep(2.5)
    print('Not yet joined...')

print('Joined')

s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)

s.setsockopt(socket.SOL_LORA, socket.SO_DR, 5)

s.setblocking(True)

s.send(bytes([0x01, 0x02, 0x03]))

s.setblocking(False)

data = s.recv(64)
print(data)
