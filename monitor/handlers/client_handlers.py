# 客户端处理程序
import tornado.web
import tornado.gen
import tornado.ioloop
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
import json

from controllers import *


# 获取当前实例信息
class ClientGetInstanceHandler(tornado.web.RequestHandler):
    def get(self):
        result = ClientController.GetInstanceInfo()
        self.write(json.dumps(result))


# 保存上传的控制信息
class ClientConnectInstanceHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.ConnectInstance(sInstanceID)
        self.write(json.dumps(result))


# 读取当前船舶状态参数
class ClientGetParamHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.GetShipParam(sInstanceID)
        self.write(json.dumps(result))

