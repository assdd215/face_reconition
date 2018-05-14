#encoding=utf-8
import urllib
import urllib2
import json
import base64
import os
import csv
import pandas as pd

base_path = "/Users/aria/MyDocs/pics/test"
base_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
api_key = "f2Vuu76ofE-oz8CEhfqoxiWJJExzwck6"
api_secret = "4y4cA2ntPaBK3wRjxRs-5GDksC-tbZYe"

fluster_array = ["1359895115.jpg","1495271052.jpg","2105691685.jpg","2040061452.jpg","1515644505.jpg","1255059385.jpg","1452510172.jpg","1298008629.jpg","1220301935.jpg","1345686379.jpg","2181902729.jpg","2155298690.jpg","1502416970.jpg",
                 "1475721728.jpg","1444313114.jpg","1371066660.jpg","1350560622.jpg",".DS_Store","2202777503.jpg","1328923461.jpg","1480467035.jpg","1455932473.jpg","1490634094.jpg","1457491666.jpg",
                 "1422070674.jpg","1478907419.jpg","1418227845.jpg","1477203589.jpg","1482231144.jpg","2254651788.jpg","1439192854.jpg","1460566169.jpg","1491862425.jpg","1503431302.jpg","1482110521.jpg",
                 "1333001261.jpg","1499837404.jpg","1425987350.jpg","1451917789.jpg","1312115941.jpg","1507759681.jpg","1453727761.jpg","1330049763.jpg","1460619294.jpg","1326396297.jpg","1236596583.jpg",
                 "1444605659.jpg","1451762272.jpg","1223135889.jpg","1497234650.jpg","1482107280.jpg","1430388594.jpg","1466486860.jpg","1427715710.jpg","1242171691.jpg","1504995644.jpg","1397890933.jpg",
                 "1317742503.jpg","1405973079.jpg","1292609766.jpg","1377371903.jpg","1330905621.jpg"]

class Confidence(object):
    file = ""
    target = ""
    value = 0.0

    def __init__(self,file,target,value):
        self.file = file
        self.target = target
        self.value = value


def comp(data1,data2):
    if data1.value == data2.value:
        return 0
    if data1.value < data2.value:
        return 1
    if data1.value > data2.value:
        return -1


def main(target):
    target_list = os.listdir(base_path)

    for target in target_list:
        if target in fluster_array:
            print("target in fluster name:%s"%target)
            continue
        file_list = os.listdir(base_path)
        if target not in file_list:
            return
        f1 = open(os.path.join(base_path,target))
        f1_base_64 = base64.b64encode(f1.read())
        f1.close()
        confidence_result = []
        print("start requesting......... name:%s" %target)
        for file in file_list:
            if file == target:
                continue
            if file == '.DS_Store':
                continue
            f = open(os.path.join(base_path,file))
            f_base_64 = base64.b64encode(f.read())
            f.close()
            content = {
            'api_key': api_key,
            'api_secret': api_secret,
            'image_base64_1': f1_base_64,
            'image_base64_2': f_base_64
            }
            data = urllib.urlencode(content)
            req = urllib2.Request(url=base_url, data=data)
            try:
                res = urllib2.urlopen(req)
                result = json.loads(res.read())
                if res.code == 200:
                    try:
                        con = Confidence(file,target,float(result['confidence']))
                    except Exception,e:
                        print(e.message)
                        print(result)
                        continue
                    confidence_result.append(con)
                    print("finish: %s, the confidence: %f"%(con.file,con.value))
                else:
                    print("code error: %s  file is :%s"%(str(res.code),file))
            except urllib2.URLError,e:
                print e.reason
        confidence_result.sort(cmp=comp)
        csv_file = open('result3.csv', 'a')
        writer = csv.writer(csv_file)
        name_row = [target]
        writer.writerow(name_row)
        file_row = []
        value_row = []
        for item in confidence_result:
            file_row.append(item.file)
            value_row.append(item.value)
        writer.writerow(file_row)
        writer.writerow(value_row)
        csv_file.close()
        print("save to csv:%s" % file)


def compare_and_count():
    verify_set = "result3.csv"
    test_set = "test_result.csv"
    verify_count = 7
    test_count = 15
    verify_set = csv.reader(open(verify_set,'r'))
    test_set = csv.reader(open(test_set,'r'))
    verify_similar_array = []
    test_similar_array = []
    target_array =[]

    times = 0
    for row in verify_set:
        if times == 0:
            target_array.append(row)
        if times == 1:
            verify_similar_array.append(row)
        times = (times + 1) % 3
    times = 0
    for row in test_set:
        if times == 1:
            test_similar_array.append(row)
        times = (times + 1) % 3

    for i in range(len(verify_similar_array)):
        verify_queue = verify_similar_array[i][0:verify_count]
        test_queue = test_similar_array[i][0:test_count]
        hit_num = 0
        for item in test_queue:
            if item in verify_queue:
                hit_num = hit_num + 1
        print("target pic:%s   hit num:%d"%(target_array[i],hit_num))







if __name__ == '__main__':
    compare_and_count()
