# 数据库处理区
import time
import pymongo
from only import *


# 数据库
class CDatabase(CSingleton):
    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient("localhost", 27123)
        db = client.monitor  # 数据库的名字
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


    #获取船舶数据字典，按船号索引
    def GetInstanceDataByID(self, iInstanceID):
        nameList = []
        for sName in self.db.collection_names():
            strList = sName.split('_')
            if len(strList) < 3:
                continue
            if strList[2] == str(iInstanceID):
                nameList.append(sName)

        if not nameList:
            return

        dAllData = {}
        for sName in nameList:
            dataList = []
            for dData in self.db[sName].find():
                del dData["_id"]
                dataList.append(dData)
            strList = sName.split('_')
            if len(strList) == 4:
                s = 'd' + strList[3]
            elif len(strList) == 5:
                s = 'd' + strList[3] + '_' + strList[4]

            dAllData[s] = dataList

        return dAllData