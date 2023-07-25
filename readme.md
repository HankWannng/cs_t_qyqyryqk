## update
- 20230725 疑似人员定位系统请求频繁崩溃？

## 开发区接口地址
http://36.153.213.27:7777/api/TSZY/t_qyqyryqk/add

## 数据流转流程
人员定位接口>>MQTT>>订阅至开发区/OA订阅展示

## 数据规范
```
[
    {
        "JsonContent": {
            "dataId": "90134c28c31b49ea85e17bb90ff32eef", //uuid
            " enterpriseId": "123456789",//企业编码
            " collectTime ": "20180615123456",//采集时间戳，格式yyyyMMddHHmmss
            " companyPersonNum ": 4,//当前时间企业内人数
            "dataA": [
                {
                    " regionName ": "二道门外",
                    " regionType ": "1",
                    " regionPersonNum ": 1,
                    "dataB": [
                        {
                            " zjhm1": "300130200009083058",
                            " ryxm1": "张三",
                            " ssdw1": "一车间"
                        }
                    ]
                },
                {
                    " regionName ": "二道门内非风险区域",
                    " regionType ": "2",
                    " regionPersonNum ": 1,
                    "dataB": [
                        {
                            " zjhm1": "300130200009083058",
                            " ryxm1": "张三",
                            " ssdw1": "一车间"
                        }
                    ]
                },
                {
                    " regionName ": "二道门内风险四色图区域",
                    " regionType ": "3",
                    " regionPersonNum ": 2,
                    "dataB": [
                        {
                            " sstId": "90134c28c31b49ea85e17bb90ff32eef",
                            " sstqymc ": "红色区域",
                            " sstqyrs ": 1,
                            " sstfxdj": "1",
                            "dataC": [
                                {
                                    " zjhm ": "300130200009083058",
                                    " ryxm ": "张三",
                                    " ssdw ": "一车间"
                                }
                            ]
                        },
                        {
                            " sstId": "90134c28c31b49ea85e17bb90ff32eef",
                            " sstqymc ": "黄色区域",
                            " sstqyrs ": 1,
                            " sstfxdj": "2",
                            "dataC": [
                                {
                                    " zjhm ": "300130200009083058",
                                    " ryxm ": "张三",
                                    " ssdw ": "一车间"
                                }
                            ]
                        }
                    ]
                }
            ]
        },
        "UUID": "string",
        "CREATE_TIME": "string",
        "CREATE_BY": "string",
        "UPDATE_TIME": "string",
        "UPDATE_BY": "string",
        "DELETE_MARK": "string"
    }
]
```

## 字段解析
- UUID 随机生成
- 人员信息JSON字符
    - dataID uuid
    - enterpriseId 企业编码

## 配置文件内更改json
```
{
    "fxsstpath": "conf/fxsst.xlsx",
    "logpath": "Logs/app.log",
    "post_url": "http://36.153.213.27:7777/api/TSZY/t_qyqyryqk/add",
    "m_url": "http://192.168.228.83:7000/CHANGCHUN/"
}
```
fxsstpath 风险四色图信息excel表地址
logpath 日志记录地址
post_url 双重预防信息化接口
m_url 人员定位接口