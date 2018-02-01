# coding=utf-8

from only import *
from model import *


class CGlobalManager(CSingleton):
    m_InstanceDict = {}
    m_btVideoData = None
    m_sMessage = ""

    def __init__(self):
        pass

    #创建一个新的实例
    def CreateNewInstance(self, dData):
        oInstance = CInstance()
        oInstance.Init(dData)
        iID = oInstance.GetInstanceID()
        self.m_InstanceDict[iID] = oInstance
        print(self.m_InstanceDict)
        return iID


    #结束一个实例
    def FinishInstance(self, dData):
        iID = dData[INSTANCE_DATA_ID]
        lTime = dData[INSTANCE_DATA_TIME]
        dInfo = CDatabase().SearchInstanceInfoByID(iID)
        if not dInfo:
            return False

        dInfo[DATABASE_INSTANCE_INFO_FINISH_TIME] = lTime
        CDatabase().UpdateFinishInstanceInfo(dInfo)
        del self.m_InstanceDict[iID]
        return True

    #根据ID获取实例
    def GetInstanceByID(self, iID):
        return self.m_InstanceDict.get(iID, None)

    #获取当前运行的实例信息
    def GetInstanceInfo(self):
        if not self.m_InstanceDict:
            return {}

        dData = {}
        for iID, oInstance in self.m_InstanceDict.items():
            dInstanceInfo = {}
            dInstanceInfo[INSTANCE_DATA_NAME] = oInstance.GetInstanceName()
            dInstanceInfo[INSTANCE_DATA_DESP] = oInstance.GetInstanceDesp()
            dInstanceInfo[INSTANCE_DATA_AMOUNT] = oInstance.GetInstanceShipAmount()
            dInstanceInfo[INSTANCE_DATA_SHAPE] = oInstance.GetInstanceShipInfo()
            dInstanceInfo[INSTANCE_DATA_TIME] = oInstance.GetCreateTime()
            dData[iID] = dInstanceInfo

        return dData

    #当前实例心跳包连接
    def ConnectInstance(self, iInstanceID):
        if iInstanceID in list(self.m_InstanceDict.keys()):
            return {INSTANCE_DATA_RUNNING: True}
        else:
            return {INSTANCE_DATA_RUNNING: False}

    #获取船舶实验数据
    def GetShipParam(self, iInstanceID):
        oInstance = self.m_InstanceDict.get(iInstanceID, None)
        if not oInstance:
              return {}

        dData = oInstance.GetShipParam()
        return dData

    # 获取参考线信息
    def GetRefLineData(self, iInstanceID):
        oInstance = self.m_InstanceDict.get(iInstanceID, None)
        if not oInstance:
              return {}

        dData = oInstance.GetRefLineData()
        return dData

    def SaveVideoData(self, btData):
        self.m_btVideoData = btData

    # 获取视频数据
    def GetVideoData(self):
        print(type(self.m_btVideoData))
        return self.m_btVideoData
        # oInstance = self.m_InstanceDict[iInstanceID]
        # if not oInstance:
        #       return {}
        #
        # data = oInstance.GetVideoData()
        # return data

    # 获取实验存储在数据库的所有数据

    def SaveMessage(self, message):
        self.m_sMessage = message

    def GetMessage(self):
        return self.m_sMessage
