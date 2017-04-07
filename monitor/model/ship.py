# coding=utf-8

from only import *
from model.database import CDatabase


class CShip(object):
    def __init__(self):
        self.m_ID = -1  # 船只ID，从0开始
        self.m_Shape = 0
        self.m_ParamDict = {}

        self.m_DBSet = None

    def Init(self, iID, iShape):
        self.m_ID = iID
        self.m_Shape = iShape

    def BindDBSet(self, oDBSet):
        self.m_DBSet = oDBSet

    def UpdateParam(self, dParam):
        self.m_ParamDict = dParam
        CDatabase().UpdateShipParam(self.m_DBSet, dParam)


    ##---------------对外接口---------------##

    #获取型号
    def GetShape(self):
        return self.m_Shape

    #获取实验数据
    def GetParam(self):
        return self.m_ParamDict