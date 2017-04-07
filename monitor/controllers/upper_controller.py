# 上位机控制器

from only import *
from model import *


class UpperController(CSingleton):
    def __init__(self):
        pass

    # 开始新的航行实例
    @staticmethod
    def StartNewInstance(dData):
        try:
            iID = CGlobalManager().CreateNewInstance(dData)
            return {
                "status": True,
                "resp": {"id": iID}
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }

    # 结束航行实例
    @staticmethod
    def FinishInstance(dData):
        try:
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
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
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

        try:
            oShip.UpdateParam(dParam)
            return {
                "status": True,
                "resp": {}
            }
        except Exception as e:
            return {
                "status": False,
                "error": str(e)
            }


    # 获取控制信息，当存在信息时返回
    @staticmethod
    def GetControlData():
        pass