import socket

SOCK_PATH = "qemu-monitor-socket"

class QEMUGPIOManager(object):
    def __init__(self, sock_path=SOCK_PATH):
        self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        self.sock.connect(sock_path)

    def send_command(self, command):
        command += "\n"  # Asegúrate de agregar un salto de línea al final del comando
        self.sock.sendall(command.encode())
        return self.receive_response()

    def receive_response(self):
        response = self.sock.recv(4096).decode()
        return response

    def close(self):
        self.sock.close()

if __name__ == "__main__":
    print("[ ] QEMU GPIO manager")
    print("[ ] Connecting to QEMU socket")

    qemu_gpio = QEMUGPIOManager()

    try:
        while True:
            cmd = input('(gpio)> ')
            if cmd.lower() == "exit":
                break
            response = qemu_gpio.send_command(cmd)
            print(response)

    finally:
        qemu_gpio.close()
