import socket
import threading



class Listener(threading.Thread):

    def __init__(self, name, port, proto):
        super().__init__(name=name)
        self._running = True
        if proto == "both":
            # self.svr_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # self.svr_tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.svr_tcp.bind(("0.0.0.0", port))
            # self.svr_tcp.listen()

            self.svr_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.svr_udp.bind(("0.0.0.0", port))

        # self.svr_socket.bind(("0.0.0.0", port))
        # self.svr_socket.listen()

    def run(self):
        while self._running:
            print("shit")
            # conn_tcp, client_addr_tcp = self.svr_tcp.accept()
            # conn_udp, client_addr_udp = self.svr_udp.accept()
            data, addr = self.svr_udp.recv(4096)
            print(data)
            # while self._running:
            #     print("here")
            #     udata, addr = self.svr_udp.recv(4096)
            #     print(udata)
            #     print(addr)
            #     data = conn_tcp.recv(4096)
            #     print(f"Got data: {data}")
            #     s = data.decode().strip()
            #     if data:
            #         conn_tcp.sendall(f"[{s}]".encode())
            #     else:
            #         print("nodata")
            #         self._running = False
            #         break



if __name__ == "__main__":

    ports = {
        "both": [7946],
        "tcp": [2377],
        "udp": [4789]
    }

    # for k, v in ports.items():
    #     for port in v:
    #         print(k, port)
    #         lsr = Listener(str(port), port, k)
    lsr = Listener(str(10086), 10086, "both")
    lsr.start()


    # pt = Listener("shit", 10080)