# 上位机控制器

from model import *


class UpperController(CSingleton):
    def __init__(self):
        pass

    # 开始新的航行实例
    @staticmethod
    def StartNewInstance(dData):
        iID = CGlobalManager().CreateNewInstance(dData)
        return {
            "status": True,
            "resp": {"id": iID}
        }

    # 结束航行实例
    @staticmethod
    def FinishInstance(dData):
        if CGlobalManager().FinishInstance(dData):
            return {
                "status": True,
                "resp": {}
            }
        else:
            return {
                "status": False,
                "error": "数据库未记录当前实例信息"
            }

    # 更新船舶数据
    @staticmethod
    def UpdateParam(iInstanceID, iShipID, dParam):
        oInstance = CGlobalManager().GetInstanceByID(iInstanceID)
        if not oInstance:
            return {
                "status": False,
                "error": "服务器当前未存在该实例，ID＝%d" % iInstanceID
            }

        oShip = oInstance.GetShipByID(iShipID)
        if not oShip:
            return {
                "status": False,
                "error": "服务器当前未存在该实例下的船只，ID＝%d" % iShipID
            }

        oShip.UpdateParam(dParam)
        return {
            "status": True,
            "resp": {}
        }


    # 获取控制信息，当存在信息时返回
    @staticmethod
    def GetControlData(iInstanceID):
        iTime = 0
        while 1:
            oInstance = CGlobalManager().GetInstanceByID(iInstanceID)
            if iTime > 50000000 or not oInstance:
                return {
                    "status": False,
                    "resp": {}
                }
            sControlData = oInstance.GetControlData()
            if sControlData:
                oInstance.ClearControlData()
                return {
                    "status": True,
                    "resp": sControlData
                }

            iTime += 1


    # 更新参考线信息
    @staticmethod
    def UpdateRefLine(iInstanceID, iShipID, dData):
        oInstance = CGlobalManager().GetInstanceByID(iInstanceID)
        if not oInstance:
            return {
                "status": False,
                "error": "服务器当前未存在该实例，ID＝%d" % iInstanceID
            }

        oShip = oInstance.GetShipByID(iShipID)
        if not oShip:
            return {
                "status": False,
                "error": "服务器当前未存在该实例下的船只，ID＝%d" % iShipID
            }

        oShip.UpdateRefLine(dData)
        return {
            "status": True,
            "resp": {}
        }

    # 更新视频信息
    @staticmethod
    def UpdateVideo(data):
        CGlobalManager().SaveVideoData(data)
        return {
            "status": True,
            "resp": {}
        }

    # 更新状态反馈信息
    @staticmethod
    def UpdateMessage(message):
        CGlobalManager().SaveMessage(message)
        return {
            "status": True,
            "resp": {}
        }