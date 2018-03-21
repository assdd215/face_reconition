# face_reconition
Use facenet to achieve face reconition and sort by similarity



# 基于FaceNet的人脸识别

该工程实现的功能是用户输入人像图片或图片集合，算法将图片映射成为特征向量。
算法根据特征向量计算两张图片之间的相似度，将输入的图片与数据库中现有的所有图片进行相似度比较，并根据相似度对图片进行排序后返回top-N。

## 备注
因个人项目需要，在做识别之前会将图片库的所有图片做一次映射后把特征向量保存下来，之后再对输入的图片与图片库红的图片进行对比。暂时时间关系就不对这个逻辑进行修改了。以后想起来的时候在修改。

同时考虑到可能存在输入的图片数据库不存在，当该图片的id在数据库中不存在时，便将该图片进行映射并保存至数据库中。

## 使用注意

0、请保证输入的图片命名为不重复的float浮点字。

1、下载训练好的模型 **20170512-110547.pb**

下载地址：https://drive.google.com/file/d/0B5MzpY9kBtDVZ2RpVDYwWmxoSUk/edit

2、下载好的模型放在facenet/facenet/model/ 文件夹下

3、修改predeal.py中的model、base_img_path等变量的路径。

4、修改main.py中的model、database_file等变量的路径
