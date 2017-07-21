#程序入口
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from handlers import *

define("port", default=8002, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/monitor/upper/start_instance", upper_handlers.UpperStartInstanceHandler),
                    (r"/monitor/upper/finish_instance", upper_handlers.UpperFinishInstanceHandler),
                    (r"/monitor/upper/update_param", upper_handlers.UpperUpdateParamHandler),
                    (r"/monitor/upper/get_control/(\w+)", upper_handlers.UpperGetControlDataHandler),
                    (r"/monitor/upper/update_refline", upper_handlers.UpperUpdateRefLineHandler),
                    (r"/monitor/upper/update_video", upper_handlers.UpperUpdateVideoHandler),

                    (r"/monitor/client/get_instance", client_handlers.ClientGetInstanceHandler),
                    (r"/monitor/client/connect_instance/(\w+)", client_handlers.ClientConnectInstanceHandler),
                    (r"/monitor/client/get_param/(\w+)", client_handlers.ClientGetParamHandler),
                    (r"/monitor/client/control", client_handlers.ClientControlHandler),
                    (r"/monitor/client/get_refline/(\w+)", client_handlers.ClientGetRefLineHandler),
                    (r"/monitor/client/get_video", client_handlers.ClientGetVideoHandler),
                    (r"/monitor/client/get_data/(\w+)", client_handlers.ClientGetDataHandler),
                    ]

        tornado.web.Application.__init__(self, handlers, debug=True)

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()