# coding=utf-8

from only import *
from model.database import *
from model.ship import *


#航行实例
class CInstance(object):

    def __init__(self):
        self.m_iID = 0
        self.m_sName = ""
        self.m_sDesp = ""
        self.m_iShipAmount = 0
        self.m_ShipDict = {}
        self.m_lCreateTime = 0

    #初始化实例
    def Init(self, dData):
        self.m_sName = dData[INSTANCE_DATA_NAME]
        self.m_sDesp = dData[INSTANCE_DATA_DESP]
        self.m_iShipAmount = dData[INSTANCE_DATA_AMOUNT]
        self.m_lCreateTime = dData[INSTANCE_DATA_TIME]
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
        for iID in range(self.m_iShipAmount):
            oShip = CShip()
            iShape = SHIP_SHAPE_DICT[dData[INSTANCE_DATA_SHAPE][iID]]
            shapeDict[str(iID)] = iShape
            oShip.Init(iID, iShape)
            #绑定数据库数据集
            oDBSet = CDatabase().CreateNewShipSet(dData[INSTANCE_DATA_TIME], self.m_iID, iID)
            oShip.BindDBSet(oDBSet)

            self.m_ShipDict[iID] = oShip

        dNewData[DATABASE_INSTANCE_INFO_SHIP_SHAPE] = shapeDict
        CDatabase().InsertInstanceInfo(dNewData)



    ##---------------对外接口---------------##

    #获取实例ID
    def GetInstanceID(self):
        return self.m_iID

    #获取船
    def GetShipByID(self, iID):
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
        for tItem in self.m_ShipDict:
            shipInfoDict[tItem[0]] = tItem[1].GetShape()

        return shipInfoDict

    def GetCreateTime(self):
        return self.m_lCreateTime

    def GetShipParam(self):
        dData = {}
        if not self.m_ShipDict:
            return dData

        for tItem in self.m_ShipDict.items():
            dData[tItem[0]] = tItem[1].GetParam()

        return dData