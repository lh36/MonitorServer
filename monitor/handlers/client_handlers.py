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


# 实例心跳包
class ClientConnectInstanceHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.ConnectInstance(sInstanceID)
        self.write(json.dumps(result))


# 读取当前船舶状态参数
class ClientGetParamHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.GetShipParam(sInstanceID)
        self.write(json.dumps(result))


# 读取当前参考线信息
class ClientGetRefLineHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.GetRefLineData(sInstanceID)
        self.write(json.dumps(result))

# 获取控制信息
class ClientControlHandler(tornado.web.RequestHandler):
    def post(self):
        dData = {
            SHIP_DATA_INSTANCE_ID: self.get_argument(SHIP_DATA_INSTANCE_ID),
            SHIP_DATA_CONTROL: self.get_argument(SHIP_DATA_CONTROL),
        }
        result = ClientController.SaveControlData(dData)
        self.write(json.dumps(result))

# 获取视频数据
class ClientGetVideoHandler(tornado.web.RequestHandler):
    def get(self):
        result = CGlobalManager().GetVideoData()
        self.write(result)


# 获取状态数据
class ClientGetMessageHandler(tornado.web.RequestHandler):
    def get(self):
        result = CGlobalManager().GetMessage()
        self.write(result)

# 获取实验数据
class ClientGetDataHandler(tornado.web.RequestHandler):
    def get(self, sInstanceID):
        result = ClientController.GetData(sInstanceID)
        self.write(result)