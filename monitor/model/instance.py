# coding=utf-8

from model.ship import *
import threading
import time


#航行实例
class CInstance(object):

    def __init__(self):
        self.m_iID = 0
        self.m_sName = ""
        self.m_sDesp = ""
        self.m_iShipAmount = 0
        self.m_ShipDict = {}
        self.m_lCreateTime = 0
        self.m_lLastTime = 0
        self.m_sControlData = ""
        self.m_Timer = None
        self.m_Data = None

    #初始化实例
    def Init(self, dData):
        self.m_sName = dData[INSTANCE_DATA_NAME]
        self.m_sDesp = dData[INSTANCE_DATA_DESP]
        self.m_iShipAmount = dData[INSTANCE_DATA_AMOUNT]
        self.m_lCreateTime = dData[INSTANCE_DATA_TIME]
        self.m_lLastTime = time.time()
        self.m_iID = CDatabase().GetNewInstanceID()
        dNewData = {
            DATABASE_INSTANCE_INFO_ID: self.m_iID,
            DATABASE_INSTANCE_INFO_NAME: self.m_sName,
            DATABASE_INSTANCE_INFO_DESP: self.m_sDesp,
            DATABASE_INSTANCE_INFO_SHIP_AMOUNT: self.m_iShipAmount,
            DATABASE_INSTANCE_INFO_CREATE_TIME: self.m_lCreateTime,
        }

        shapeDict = {}
        #生成船舶对象至船舶字典
        for iID in range(1, self.m_iShipAmount + 1):
            oShip = CShip() # 创建该船
            iShape = SHIP_SHAPE_DICT[dData[INSTANCE_DATA_SHAPE][iID - 1]] # 设置船型
            shapeDict[str(iID)] = iShape # 船型临时变量字典
            oShip.Init(iID, iShape) # 根据船号船型初始化船
            #绑定数据库数据集
            oDataDBSet, oRefLineDBSet = CDatabase().CreateNewShipSet(dData[INSTANCE_DATA_TIME], self.m_iID, iID)
            oShip.BindDBSet(oDataDBSet, oRefLineDBSet)

            self.m_ShipDict[iID] = oShip

        dNewData[DATABASE_INSTANCE_INFO_SHIP_SHAPE] = shapeDict
        CDatabase().InsertInstanceInfo(dNewData)

        #生成定时器
        self.m_Timer = threading.Timer(10 * 60 + 10, self.TimerFinishInstance)
        self.m_Timer.start()

    #定时器调用，结束丢弃的实例
    def TimerFinishInstance(self):
        if time.time() - self.m_lLastTime > 10 * 60:
            dData = {
                INSTANCE_DATA_ID: self.m_iID,
                INSTANCE_DATA_TIME: time.time()
            }
            self.m_Timer.cancel()
            self.m_Timer = None
            from model.manager import CGlobalManager
            CGlobalManager().FinishInstance(dData)
        else:
            self.m_Timer.cancel()
            self.m_Timer = threading.Timer(10 * 60 + 10, self.TimerFinishInstance)
            self.m_Timer.start()

    ##---------------对外接口---------------##

    #获取实例ID
    def GetInstanceID(self):
        return self.m_iID

    #获取船
    def GetShipByID(self, iID):
        self.m_lLastTime = time.time()
        return self.m_ShipDict.get(iID, None)

    def GetInstanceName(self):
        return self.m_sName

    def GetInstanceDesp(self):
        return self.m_sDesp

    def GetInstanceShipAmount(self):
        return self.m_iShipAmount

    def GetInstanceShipInfo(self):
        if not self.m_ShipDict:
            return {}

        shipInfoDict = {}
        for tItem in self.m_ShipDict.items():
            shipInfoDict[tItem[0]] = tItem[1].GetShape()

        return shipInfoDict

    def GetCreateTime(self):
        return self.m_lCreateTime

    # 获取实验数据
    def GetShipParam(self):
        dData = {}
        if not self.m_ShipDict:
            return dData

        for tItem in self.m_ShipDict.items():
            dData[tItem[0]] = tItem[1].GetParam()

        return dData

    # 获取参考线信息
    def GetRefLineData(self):
        dData = {}
        if not self.m_ShipDict:
            return dData

        for tItem in self.m_ShipDict.items():
            dData[tItem[0]] = tItem[1].GetRefLine()

        return dData

    # 保存控制信息
    def SaveControlData(self, sData):
        self.m_sControlData = sData

    def GetControlData(self):
        return self.m_sControlData

    def ClearControlData(self):
        self.m_sControlData = ""

    # 保存视频数据
    def UpdateVideo(self, data):
        self.m_Data = data
        print(data)

    def GetVideoData(self):
        return  self.m_Data