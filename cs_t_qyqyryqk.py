#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2023/06/07 09:59:48
@Author      :HankWang
@version      :1.0
'''

from __future__ import print_function

import time
import json
import uuid
import datetime
import requests
import pandas as pd
import random
import re
from tools.readexcelinfo import read_fxfq_info, find_fxsst_info
from tools.get_wwyt_info import get_wwyt_data
from tools.post_cckfq_data import post_cckfq_data
import tools.identity as identity
from tools.logger import Logger
from tools.ap_scheduler import Bscheduler


def getAreainfo_data(df, result):
    edmw_list, edmn_list = [], []
    for i in result['data']:
        dataC = []
        # datetime = time_now
        area = i['areaId']
        areaName = i['areaName']
        personList = i['personList']
        if personList != []:
            for ii in personList:
                ryxm1 = ii['empName']
                ryxm2 = re.sub("[A-Za-z0-9\!\%\[\]\,\。]", "", ryxm1)  # 正则去英文
                # print(ryxm2)
                random_sex = random.randint(0, 1)
                ran_id = identity.IdNumber.generate_id(random_sex)
                if "车辆" not in ryxm1:
                    infor_dict = {
                        "zjhm1": ran_id,  # todo
                        "ryxm1": ryxm1,
                        "ssdw1": areaName
                    }
                    dataC.append(infor_dict)
        if area in [217, 218, 219]:
            edmw_list += dataC
        else:
            ss_data = find_fxsst_info(df, area)
            if ss_data != []:
                dataC_dict = {
                    "sstId": ss_data[4],  # 企业风险四色图区域主键ID     五位一体获取 ---ok
                    "sstqymc": ss_data[2],  # 企业风险四色图区域名称  --- ok
                    "sstqyrs": len(dataC),  # 四色图区域人数
                    # 企业风险四色图区域风险等级(1：一级；2：二级；3：三级；4：四级)
                    "sstfxdj": ss_data[3].split(":")[0],
                    "dataC": dataC
                }
        if dataC != []:
            edmn_list.append(dataC_dict)
    return edmw_list, edmn_list


# print(payload_data['JsonContent'])


def save_json(save_path, data):
    assert save_path.split('.')[-1] == 'json'
    with open(save_path, 'w', encoding="utf8") as file:
        json.dump(data, file, ensure_ascii=False)


def job1():
    # 产生随机UUID
    m_uuid = str(uuid.uuid4())
    dataid_uuid = str(uuid.uuid4())
    # print(m_uuid)  # 随机UUID
    # 时间
    time_now = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # 企业编码
    enterpriseId = '320510457'
    # 获取风险四色图信息
    df = read_fxfq_info(json_conf['fxsstpath'])
    # 获取五位一体人员定位数据
    result = get_wwyt_data(json_conf['m_url'])
    # 按需求拼接各区域的人员信息，人员身份证TD
    edmw_list, edmn_list = getAreainfo_data(df, result)
    # 区域类型
    # 1:二道门外(217/218/219)；2:二道门内非风险区域
    edmw_dataA = {
        "regionName": "二道门外",
        "regionType": "1",
        "regionPersonNum": len(edmw_list),
        "dataB": edmw_list}

    # 类型3
    edmn_dataA = {
        "regionName": "二道门内四色图区域",
        "regionType": "3",
        "regionPersonNum": len(edmn_list),
        "dataB": edmn_list[:20]}

    JsonContent_dict = {
        "dataId": dataid_uuid,
        "enterpriseId": enterpriseId,  # 企业编码
        "collectTime ": time_now,  # 采集时间戳，格式yyyyMMddHHmmss
        "companyPersonNum ": 1,  # companyPersonNum,  # 当前时间企业内人数 todo
        "dataA": [edmw_dataA, edmn_dataA]
    }

    qyqyry_dict = [{
        "JsonContent": str(JsonContent_dict),
        "UUID": m_uuid,
        "CREATE_TIME": time_now,
        "CREATE_BY": "袁维杰",
        "UPDATE_TIME": time_now,
        "UPDATE_BY": "袁维杰",
        "DELETE_MARK": 0

    }]
    # ensure_ascii=False 使用后可解决中文乱码问题，但上抛会失败？
    payload_data = json.dumps(qyqyry_dict)
    # 保存数据
    # save_json("./data.json", (JsonContent_dict))
    # 上抛
    x = post_cckfq_data(payload_data,json_conf['post_url'])
    # print(x)
    log = Logger(json_conf['logpath'], level='debug')
    log.logger.debug(x)
    # log.logger.debug(f"{x}\n{qyqyry_dict}")


def conf():
    with open('conf/config.json',"r") as cf:
        json_conf = json.load(cf)
    return json_conf
    

def main():
    global json_conf
    json_conf = conf()
    Bscheduler(job1)


if __name__ == "__main__":
    # job1()
    # json_conf = conf()
    main()
