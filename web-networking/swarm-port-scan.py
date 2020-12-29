import socket
import threading
import multiprocessing


class Listener(threading.Thread):

    def __init__(self, name, port, proto):
        super().__init__(name=name)
        self._running = True
        self._proto = proto
        print("init", proto, port)
        try:
            if proto == "tcp":
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                # Use socket in TIME_WAIT state
                self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
                print("here", port)
                self.sock.bind(("0.0.0.0", port))
                self.sock.listen()
            else:
                self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                self.sock.bind(("0.0.0.0", port))
        except OSError as err:
            print(port, err)

    def run(self):
        print(self._proto)
        while self._running:
            if self._proto == "tcp":
                tcp_conn, addr = self.sock.accept()
                print("accept tcp connection", addr)
                th = threading.Thread(target=self._handle_tcp_conn, args=(tcp_conn, addr))
                th.daemon = True
                th.start()
            else:
                data, addr = self.sock.recvfrom(4096)
                print("udp", addr)
                self.sock.sendto(data, addr)

    def _handle_tcp_conn(self, connection, address):
        try:
            while True:
                raw_data, addr = connection.recvfrom(4096)
                data = raw_data.decode().strip()
                print(data)
                if data == "":
                    break
                connection.sendto(raw_data, address)
        # except:
        #     print("exception caught")
        finally:
            connection.close()


if __name__ == "__main__":
    target_ips = ["172.16.66.6"]

    swarm_ports = {
        # "tcp": [2377, 7946, 26500, 26501, 80, 443],
        "tcp": [10086, 10000],
        # "udp": [24789, 7946]
        # "udp": [24789]
    }

    listeners = []
    # lsr = Listener(str(10086), 10086, "tcp")

    for proto, ports in swarm_ports.items():
        for port in ports:
            lsr = Listener(str(port), port, proto)
            listeners.append(lsr)


    for listener in listeners:
        listener.start()
        listener.join()
