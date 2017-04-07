# 客户端控制器

from only import *
from model import *


class ClientController(object):
    def __init__(self):
        pass


    # 获取当前实例信息
    @staticmethod
    def GetInstanceInfo():
        try:
            result = CGlobalManager().GetInstanceInfo()
            return {
                "status": True,
                "resp": result
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }

    # 连接当前实例,心跳包
    @staticmethod
    def ConnectInstance(sInstanceID):
        try:
            iInstanceID = int(sInstanceID)
            result = CGlobalManager().ConnectInstance(iInstanceID)
            return {
                "status": True,
                "resp": result
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }

    # 获取船只实验数据
    @staticmethod
    def GetShipParam(sInstanceID):
        try:
            iInstanceID = int(sInstanceID)
            result = CGlobalManager().GetShipParam(iInstanceID)
            return {
                "status": True,
                "resp": result
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }