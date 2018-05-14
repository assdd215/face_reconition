import base64



base_path = "/Users/aria/MyDocs/pics/test"
def get_img_stream():
    file_path = base_path + "/320.jpg"
    img_file = open(file_path,'r')
    img_stream = img_file.read()
    # img_stream = base64.b64encode(img_stream)
    return img_stream