#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Description:       :
@Date     :2023/06/21 08:33:03
@Author      :HankWang
@version      :1.0
'''
import requests
import json
# 上抛


def post_cckfq_data(payload_data,post_url = 'http://36.153.213.27:7777/api/TSZY/t_qyqyryqk/add'):
    # post_url = 'http://36.153.213.27:7777/api/TSZY/t_qyqyryqk/add'
    headers = {
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Token': '6AB810C1-D492-CBB9-6B04-D509450CAF63',
        'Connection': 'keep-alive',
        "Content-Type": "application/json",
    }

    response2 = requests.request(
        "post", post_url, data=payload_data, headers=headers)
    result2 = json.loads(response2.text)
    return result2
    # print(result2)


