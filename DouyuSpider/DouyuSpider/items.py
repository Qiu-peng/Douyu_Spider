# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuspiderItem(scrapy.Item):
    # 房间的链接
    room_link = scrapy.Field()
    # 图片的链接
    image_link = scrapy.Field()
    # 主播艺名
    nick_name = scrapy.Field()
    # 所在城市
    city = scrapy.Field()
    # 图片的磁盘路径
    image_path = scrapy.Field()
