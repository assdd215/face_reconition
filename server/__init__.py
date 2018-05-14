from flask import Flask,url_for,render_template,request,Response
import facenet.face_recognition as facenet
import utils
import json
import os

app = Flask(__name__)

@app.route("/function")
def compare():
    base_file_path = "/Users/aria/MyDocs/pics/anchors"
    print("in compare")
    file_name = request.args.get("file_name")
    n = request.args.get("n")
    result = facenet.main(test_path=os.path.join(base_file_path,file_name),top_n=n)
    str = json.dumps(result,default=facenet.data_2_json)
    print(str)
    return str

@app.route("/getResult")
def getResult():
    base_file_path = "/Users/aria/MyDocs/pics/test"
    file_names = request.args.get("file_names")
    n = request.args.get("n")
    file_names = file_names.split(',')
    new_list = []
    for name in file_names:
        new_list.append(os.path.join(base_file_path,name))
    result = facenet.main(test_path=new_list,top_n=n)
    return json.dumps(result,default=facenet.data_2_json)

@app.route("/getPic/<string:file_name>")
def getPic(file_name):
    img = file(utils.base_path + "/" + file_name)
    resp = Response(img,mimetype="image/jpeg")
    return resp

@app.route("/list")
def getList():
    base_file_path = "/Users/aria/MyDocs/pics/test"
    anchor_name_list = os.listdir(base_file_path)
    anchor_list = []
    for anchor in anchor_name_list:
        if anchor == '.DS_Store':
            continue
        anchor_list.append(facenet.SimpleData(key=anchor))
    return json.dumps(anchor_list,default=facenet.data_2_json)
