# -*- coding: utf-8 -*-

import scrapy
import os
from scrapy.pipelines.images import ImagesPipeline
from settings import IMAGES_STORE
import pymongo


class DouyuImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        # 通过ImagesPipeline，把从链接请求到的图片下载下来，下载的路径要在settings中设置好
        yield scrapy.Request(item['image_link'])

    def item_completed(self, results, item, info):

        # 取出图片路径
        image_path = [x['path'] for ok, x in results if ok]
        print image_path[0]

        # 保存图片在磁盘的路径, item中的字段，在此处赋值
        item['image_path'] = IMAGES_STORE + item['nick_name'] + ".jpg"
        print item['image_path']

        # 将图片改名  os.rename(old_name, new_name)
        os.rename(IMAGES_STORE + image_path[0], item['image_path'])
        return item

        # 保存图片在磁盘的路径


class DouyuMongoDBPipline(object):
    def __init__(self):
        # 创建MongoDB数据库连接
        self.client = pymongo.MongoClient(host="127.0.0.1", port=27017)
        # 指定MongoDB的数据库名
        self.db_name = self.client['Douyu']
        # 指定数据库表名
        self.sheet_name = self.db_name['DouyuDirector']

    def process_item(self, item, spider):
        # 向表里插入数据，参数是一个字典
        self.sheet_name.insert(dict(item))
        print "mongodb"
        return item




