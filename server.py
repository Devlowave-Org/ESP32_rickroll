import socket
import asyncio
from playsound import playsound
import atexit


class Server:

    def __init__(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind(self, port):
        self.socket.bind(("", port))
        self.socket.listen()
        self.conn , self.addr = self.socket.accept()

    async def received_message(self):
        message_bit = self.conn.recv(1024)
        message_utf8 = message_bit.decode('utf-8')
        return message_utf8

    def send_message(self, message):
        message_bit = message.encode('utf-8')
        self.conn.send(message_bit)

    def close(self):
        self.conn.close()


async def main():
    server = Server()
    server.bind(port=3132)

    while True:
        message = await server.received_message()
        print(f"Connect with {server.addr}")
        print(message)

        if message == "RICKROLL":
            server.send_message("continue")
            playsound("rickroll.mp3")
            print("The music END... wait 5 second")

        
asyncio.run(main())