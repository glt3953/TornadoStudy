import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver
import tornado.websocket
from tornado.options import define,options
define("port",default=8001,help="run on the given port",type=int)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class EchoWebSocket(tornado.websocket.WebSocketHandler):
    def open(self):
        print("WebSocket opened")

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("WebSocket closed")
def make_app():
    return tornado.web.Application([
        (r"/",EchoWebSocket)
        ])
if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
