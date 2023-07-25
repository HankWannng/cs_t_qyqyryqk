#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2023/06/20 09:59:27
@Author      :HankWang
@version      :1.0
'''

import pandas as pd

# 读取身份证信息


def read_person_info():
    file = ''
    df = pd.read_excel(file)
    return df


# 查找对应人的身份证信息
def find_person_info(df,name):
    try:
        data_list = list(df.loc[df["人员姓名"] == name].values[0])
    except:
        data_list = []
    return data_list


# 查找对应风险分区的信息
def read_fxfq_info(excel_file= r'./fxsst.xlsx'): 
    df = pd.read_excel(excel_file)
    df1 = df.dropna(axis=0)  # 去掉空值行
    df2 = df1.iloc[:, [1, 2, 3, 4, 15]]
    return df2


def find_fxsst_info(df,SSID):
    # data = df.loc[df['五位一体ID'] == SSID]
    try:
        data_list = list(df.loc[df['五位一体ID'] == SSID].values[0])
    except:
        data_list = []
    # print(data_list)
    return data_list