# 客户端控制器

from only import *
from model import *


class ClientController(object):
    def __init__(self):
        pass


    # 获取当前实例信息
    @staticmethod
    def GetInstanceInfo():
        result = CGlobalManager().GetInstanceInfo()
        return {
            "status": True,
            "resp": result
        }

    # 连接当前实例,心跳包
    @staticmethod
    def ConnectInstance(sInstanceID):
        iInstanceID = int(sInstanceID)
        result = CGlobalManager().ConnectInstance(iInstanceID)
        return {
            "status": True,
            "resp": result
        }

    # 获取船只实验数据
    @staticmethod
    def GetShipParam(sInstanceID):
        iInstanceID = int(sInstanceID)
        result = CGlobalManager().GetShipParam(iInstanceID)
        return {
            "status": True,
            "resp": result
        }

    # 获取运动参考线信息
    @staticmethod
    def GetRefLineData(sInstanceID):
        iInstanceID = int(sInstanceID)
        result = CGlobalManager().GetRefLineData(iInstanceID)
        return {
            "status": True,
            "resp": result
        }

    # 保存控制信息
    @staticmethod
    def SaveControlData(dData):
        iInstanceID = int(dData[SHIP_DATA_INSTANCE_ID])
        oInstance = CGlobalManager().GetInstanceByID(iInstanceID)
        if not oInstance:
            return {
                "status": False,
                "resp": {}
            }
        result = oInstance.SaveControlData(dData[SHIP_DATA_CONTROL])
        return {
            "status": result,
            "resp": {}
        }

    # # 获取视频数据
    # @staticmethod
    # def GetVideoData(sInstanceID):
    #     iInstanceID = int(sInstanceID)
    #     result = CGlobalManager().GetVideoData(iInstanceID)
    #     return {
    #         "status": True,
    #         "resp": result
    #     }