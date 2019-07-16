import json

import tornado.web
import tornado.websocket
import tornado.httpserver
import tornado.ioloop
from tornado.escape import json_decode
from redis import Redis, RedisError

USERS = set()

def get_minion_num():
    try:
        redis = Redis(host="localhost", port=6379, db=0)
        num = redis.get("minions")
    except RedisError:
        num = -1

    return 0 if not num else num


class Index(tornado.web.RequestHandler):
    def get(self):
        self.write("Online Minions: {}".format(get_minion_num()))

    # def post(self):
    #    print(self.request.headers)
    #    print(self.request.body)
    #    print(self.get_body_arguments("cpu"))
    #    self.data = json_decode(self.request.body)
    #    print(self.data)
    #    self.write(json.dumps({"ok": "got it"}))


class OnlineWS(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Minion online")

    def on_message(self, message):
        print(message)

    def on_close(self):
        print("Minion offline")


class Gru(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", Index),
            (r"/ws", OnlineWS)
        ]

        settings = dict(
            debug=True,
            autoreload=True,
        )

        super(Gru, self).__init__(handlers, **settings)


if __name__ == "__main__":
    http_svr = tornado.httpserver.HTTPServer(Gru())
    http_svr.listen(8000)
    tornado.ioloop.IOLoop.current().start()
