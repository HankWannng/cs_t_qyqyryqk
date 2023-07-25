#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2023/06/21 08:25:58
@Author      :HankWang
@version      :1.0
'''

import requests
import json




def get_wwyt_data(m_url = 'http://192.168.228.83:7000/CHANGCHUN/'):
    m_url = 'http://192.168.228.83:7000/CHANGCHUN/'
    getRealGps_url = m_url + "open/information/getRealGps.do?username=front&password=123456"
    getRealTotals_url = m_url + 'ajpt/getRealTotals.do'
    areainfo_url = m_url + 'open/information/getRealAreaInfo.do'
    payload = {}
    response = requests.request("GET", areainfo_url,  data=payload)
    result = json.loads(response.text)
    return result




if __name__ == "__main__":
    get_wwyt_data()

