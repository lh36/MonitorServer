# coding=utf-8

import random
import time


##--------常量定义----------##

#实例信息key
INSTANCE_DATA_ID = "id"
INSTANCE_DATA_NAME = "name"
INSTANCE_DATA_DESP = "desp"
INSTANCE_DATA_AMOUNT = "amount"
INSTANCE_DATA_SHAPE = "shape"
INSTANCE_DATA_TIME = "time"
INSTANCE_DATA_RUNNING = "running"

#实验数据key
SHIP_DATA_LAT = "lat"
SHIP_DATA_LON = "lon"
SHIP_DATA_POSX = "posX"
SHIP_DATA_POSY  = "posY"
SHIP_DATA_RUD = "rud"
SHIP_DATA_PHI = "phi"
SHIP_DATA_GPS_PHI = "gps_phi"
SHIP_DATA_SPEED = "speed"
SHIP_DATA_GEAR = "gear"
SHIP_DATA_TIME = "time"
SHIP_DATA_KP = "kp"
SHIP_DATA_KI = "ki"
SHIP_DATA_KD = "kd"
SHIP_DATA_K1 = "k1"
SHIP_DATA_K2 = "k2"
SHIP_DATA_TEM = "tem"
SHIP_DATA_PH = "pH"
SHIP_DATA_DISO = "diso"
SHIP_DATA_TUR = "tur"
SHIP_DATA_CON = "con"


SHIP_DATA_INSTANCE_ID = "instanceid"
SHIP_DATA_SHIP_ID = "shipid"

#控制信息:w(s,a,d,p)-1或c[str];
# w前,s后,d右,a左,p停止,可组合
# -后面的数字为船舶id
# 首字母为c则表示复杂命令,str的具体命令格式自行定义
SHIP_DATA_CONTROL = "control"


#船的型号
SHIP_SHAPE_A = 1
SHIP_SHAPE_B = 2
SHIP_SHAPE_C = 3
SHIP_SHAPE_DICT = {'A': SHIP_SHAPE_A,
                   'B': SHIP_SHAPE_B,
                   'C': SHIP_SHAPE_C
                   }

#参考线数据
REFLINE_FLAG = "flag"
REFLINE_POSX = "posX"
REFLINE_POSY = "posY"
REFLINE_RADIUS = "radius"
REFLINE_COUNT = "count"
REFLINE_POINTS = "points"


#数据库存储实例信息key
DATABASE_INSTANCE_INFO_SEARCH = {"flag": "InstanceInfo"}
DATABASE_INSTANCE_INFO_AMOUNT = "instance_amount"
DATABASE_INSTANCE_INFO_TOPID = "top_id"
DATABASE_INSTANCE_INFO_ID = "id"
DATABASE_INSTANCE_INFO_NAME = "name"
DATABASE_INSTANCE_INFO_DESP = "desp"
DATABASE_INSTANCE_INFO_SHIP_AMOUNT = "ship_amount"
DATABASE_INSTANCE_INFO_SHIP_SHAPE = "ship_shape"
DATABASE_INSTANCE_INFO_CREATE_TIME = "create_time"
DATABASE_INSTANCE_INFO_FINISH_TIME = "finish_time"



# 实现单列模式
class CSingleton(object):
    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            orig = super(CSingleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        return cls._instance