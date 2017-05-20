# 数据库处理区
import time
import pymongo
from only import *


# 数据库
class CDatabase(CSingleton):
    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient("localhost", 27123)
        db = client.monitor
        self.db = db
        self.instance_info_db = self.db.instance_info

    # 新建船舶数据表,以时间加序号命名
    def CreateNewShipSet(self, lTime, iInstanceID, iShipID):
        sTime = time.strftime("%Y%m%d_%H%M_", time.localtime(lTime))
        sDataSetName = sTime + str(iInstanceID) + '_' + str(iShipID)
        sRefLineSetName = sTime + str(iInstanceID) + '_' + str(iShipID) + "_ref"

        return self.db[sDataSetName], self.db[sRefLineSetName]

    #生成一个实例存储ID
    def GetNewInstanceID(self):
        dInstanceInfo = self.instance_info_db.find_one(DATABASE_INSTANCE_INFO_SEARCH)

        if not dInstanceInfo:
            #生成实例信息表
            dData = {list(DATABASE_INSTANCE_INFO_SEARCH.keys())[0]: list(DATABASE_INSTANCE_INFO_SEARCH.values())[0],
                     DATABASE_INSTANCE_INFO_AMOUNT: 0,
                     DATABASE_INSTANCE_INFO_TOPID: 0,}
            self.instance_info_db.insert_one(dData)
            return 1
        else:
            iID = dInstanceInfo[DATABASE_INSTANCE_INFO_TOPID] + 1
            dInstanceInfo[DATABASE_INSTANCE_INFO_TOPID] = iID
            dInstanceInfo[DATABASE_INSTANCE_INFO_AMOUNT] += 1
            self.instance_info_db.save(dInstanceInfo)
            return iID


    #添加实例信息
    def InsertInstanceInfo(self, dData):
        self.instance_info_db.insert_one(dData)

    #根据实例ID查找实例信息
    def SearchInstanceInfoByID(self, iID):
        dData = self.instance_info_db.find_one({DATABASE_INSTANCE_INFO_ID: iID})
        return dData

    #结束实例，更新实例信息
    def UpdateFinishInstanceInfo(self, dData):
        self.instance_info_db.save(dData)

    #更新船舶实验数据
    def InsertShipData(self, oDBSet, dData):
        oDBSet.insert_one(dData)