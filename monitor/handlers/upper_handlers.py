# 处理程序
import tornado.web
import tornado.gen
import tornado.ioloop
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor
import json

from controllers import *


# 开启航行实例
class UpperStartInstanceHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        data = {
            INSTANCE_DATA_NAME: self.get_argument(INSTANCE_DATA_NAME),
            INSTANCE_DATA_DESP: self.get_argument(INSTANCE_DATA_DESP),
            INSTANCE_DATA_AMOUNT: int(self.get_argument(INSTANCE_DATA_AMOUNT)),
            INSTANCE_DATA_SHAPE: self.get_argument(INSTANCE_DATA_SHAPE),
            INSTANCE_DATA_TIME: int(self.get_argument(INSTANCE_DATA_TIME)),
        }
        result = UpperController.StartNewInstance(data)
        self.write(json.dumps(result))


# 结束航行实例
class UpperFinishInstanceHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        data = {
            INSTANCE_DATA_ID: int(self.get_argument(INSTANCE_DATA_ID)),
            INSTANCE_DATA_TIME: int(self.get_argument(INSTANCE_DATA_TIME)),
        }
        result = UpperController.FinishInstance(data)
        self.write(json.dumps(result))


# 更新上位机船舶参数
class UpperUpdateParamHandler(tornado.web.RequestHandler):
    def post(self):
        dParam = {
            SHIP_DATA_LAT: float(self.get_argument(SHIP_DATA_LAT)),
            SHIP_DATA_LON: float(self.get_argument(SHIP_DATA_LON)),
            SHIP_DATA_POSX: float(self.get_argument(SHIP_DATA_POSX)),
            SHIP_DATA_POSY: float(self.get_argument(SHIP_DATA_POSY)),
            SHIP_DATA_RUD: float(self.get_argument(SHIP_DATA_RUD)),
            SHIP_DATA_PHI: float(self.get_argument(SHIP_DATA_PHI)),
            SHIP_DATA_GPS_PHI: float(self.get_argument(SHIP_DATA_GPS_PHI)),
            SHIP_DATA_SPEED: float(self.get_argument(SHIP_DATA_SPEED)),
            SHIP_DATA_GEAR: int(self.get_argument(SHIP_DATA_GEAR)),
            SHIP_DATA_TIME: int(self.get_argument(SHIP_DATA_TIME)),
            SHIP_DATA_KP: float(self.get_argument(SHIP_DATA_KP)),
            SHIP_DATA_KI: float(self.get_argument(SHIP_DATA_KI)),
            SHIP_DATA_KD: float(self.get_argument(SHIP_DATA_KD)),
            SHIP_DATA_K1: float(self.get_argument(SHIP_DATA_K1)),
            SHIP_DATA_K2: float(self.get_argument(SHIP_DATA_K2)),
        }
        iInstanceID = int(self.get_argument(SHIP_DATA_INSTANCE_ID))
        iShipID = int(self.get_argument(SHIP_DATA_SHIP_ID))
        result = UpperController.UpdateParam(iInstanceID, iShipID, dParam)
        self.write(json.dumps(result))


# 返回上位机请求的控制信息
class UpperGetControlDataHandler(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor()

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, sInstanceID):
        try:
            result = yield self.waitForControlData(int(sInstanceID))
            self.write(json.dumps(result))
        finally:
            self.finish()

    @run_on_executor
    def waitForControlData(self, iInstanceID):
        return UpperController.GetControlData(iInstanceID)


# 获取上位机发送的参考线
class UpperUpdateRefLineHandler(tornado.web.RequestHandler):
    def post(self):
        dData = {
            REFLINE_FLAG: int(self.get_argument(REFLINE_FLAG)),
            REFLINE_POSX: float(self.get_argument(REFLINE_POSX)),
            REFLINE_POSY: float(self.get_argument(REFLINE_POSY)),
            REFLINE_RADIUS: float(self.get_argument(REFLINE_RADIUS)),
        }
        iInstanceID = int(self.get_argument(SHIP_DATA_INSTANCE_ID))
        iShipID = int(self.get_argument(SHIP_DATA_SHIP_ID))
        result = UpperController.UpdateRefLine(iInstanceID, iShipID, dData)
        self.write(json.dumps(result))

