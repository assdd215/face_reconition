import requests
import urllib
import urllib2
import json
import base64
import csv


def main():
    base_url = "https://api-cn.faceplusplus.com/facepp/v3/compare"
    f1 = open("/Users/aria/MyDocs/pics/resize_anchors/318.jpg")
    f = open("/Users/aria/MyDocs/pics/resize_anchors/319.jpg")
    content = {
        'api_key': "f2Vuu76ofE-oz8CEhfqoxiWJJExzwck6",
        'api_secret': '4y4cA2ntPaBK3wRjxRs-5GDksC-tbZYe',
        'image_base64_1': base64.b64encode(f1.read()),
        'image_base64_2': base64.b64encode(f.read())
    }
    f1.close()
    f.close()

    data = urllib.urlencode(content)
    req = urllib2.Request(url=base_url,data=data)
    res = urllib2.urlopen(req)
    result = json.loads(res.read())
    print(result['confidence'])


def write_to_csv():
    csv_file = open('instance.csv','a')
    writer = csv.writer(csv_file)
    d1 = ["318.jpg"]
    d2 = ['319.jpg',"320.jpg"]
    d3 = ['320.jpg']
    writer.writerow(d1)
    writer.writerow(d2)

    csv_file.close()


if __name__ == '__main__':
    write_to_csv()



