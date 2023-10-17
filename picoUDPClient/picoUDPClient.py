import time
import network
import socket

#ssid = 'AXTEL_1589D4'
#password = '68395544'

cont = 0

ssid = 'LUMarteymedios_2.4'
password = '0@@LuMmx@@0'

def get_html(html_name, value):
    # open html_name (index.html), 'r' = read-only as variable 'file'
    with open(html_name, 'r') as file:
        html = file.read()
    content = html.replace(
        "<h2 id=\"analog\"></h2>", f"<h2 id=\"analog\">{value}</h2>")
    return content

def value():
    val = 2400
    return val

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.ifconfig(("192.168.1.40", "255.255.255.0", "192.168.1.254", "8.8.8.8"))
wlan.connect(ssid, password)

# Wait for connect or fail
max_wait = 10
while max_wait > 0:
    if wlan.status() < 0 or wlan.status() >= 3:
        break
    max_wait -= 1
    print('waiting for connection...')
    time.sleep(1)

# Handle connection error
if wlan.status() != 3:
    raise RuntimeError('network connection failed')
else:
    print('connected')
    status = wlan.ifconfig()
    print( 'ip = ' + status[0] )
    
UDP_IP = "192.168.1.65"
UDP_PORT = 33333
cont = 0

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
    
while True:
    print(cont)
    sock.sendto(str(cont).encode(), (UDP_IP, UDP_PORT))
    cont = cont + 1
    time.sleep(1)