import network
import espnow
from machine import Pin

# Inicializa la interfaz WiFi en modo Station
sta = network.WLAN(network.STA_IF)
sta.active(True)

# Configura el botón en el Pin 19
B1 = Pin(19, Pin.IN, Pin.PULL_UP)

# Inicializa ESP-NOW
e = espnow.ESPNow()
e.active(True)

# Agrega la dirección MAC del receptor (cambiar con la dirección real)
mac = b'\x08\xd1\xf9\xe8HX'  # MAC del receptor
e.add_peer(mac)

# Estado previo para evitar envíos redundantes
previous_state = None

# Bucle principal para enviar mensajes cuando se presione el botón
while True:
    current_state = B1.value()
    if current_state != previous_state:  # Detecta cambio en el estado del botón
        if current_state == 0:  # Botón presionado
            e.send(mac, b'ON')  # Enviar mensaje 'ON'
            print("Mensaje enviado: ON")
        else:
            e.send(mac, b'OFF')  # Enviar mensaje 'OFF'
            print("Mensaje enviado: OFF")
        previous_state = current_state  # Actualiza el estado
