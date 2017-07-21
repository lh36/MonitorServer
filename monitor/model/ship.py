# coding=utf-8

from only import *
from model.database import CDatabase


class CShip(object):
    def __init__(self):
        self.m_ID = -1  # 船只ID，从0开始
        self.m_Shape = 0
        self.m_ParamDict = {}
        self.m_RefLineDict = {}

        self.m_DataDBSet = None
        self.m_RefLineDBSet = None

    def Init(self, iID, iShape):
        self.m_ID = iID
        self.m_Shape = iShape

    def BindDBSet(self, oDataDBSet, oRefLineDBSet):
        self.m_DataDBSet = oDataDBSet
        self.m_RefLineDBSet = oRefLineDBSet


    ##---------------对外接口---------------##

    def UpdateParam(self, dParam):
        self.m_ParamDict = dParam
        CDatabase().InsertShipData(self.m_DataDBSet, dParam.copy())

    def UpdateRefLine(self, dData):
        self.m_RefLineDict = dData
        CDatabase().InsertShipData(self.m_RefLineDBSet, dData.copy())

    #获取型号
    def GetShape(self):
        return self.m_Shape

    #获取实验数据
    def GetParam(self):
        return self.m_ParamDict

    #获取参考线信息
    def GetRefLine(self):
        return self.m_RefLineDict