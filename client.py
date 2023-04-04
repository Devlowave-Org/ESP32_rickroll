import socket
import sensor
import wifi
import time

wifi.do_connect()

is_connected = False
while is_connected != True:
    try:
        client = socket.socket()
        client.connect(('10.20.0.126', 3132))
        is_connected = True
    except OSError:
        print("Can't connect")
        client.close()
        time.sleep(5)

response = "continue"
while response != "quit":
    if sensor.rickroll() == True:
        print("I sent rickroll")
        client.send("RICKROLL".encode("utf-8"))
        response = client.recv(1024).decode('utf-8')
        print(response)
        time.sleep(15)
        print("Let's rickroll again")
    else:
        print(sensor.rickroll())
        
client.close()
    