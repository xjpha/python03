# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os

class Python03Pipeline(object):
    def process_item(self, item, spider):
        return item

class StockPipeline(object):
    def __init__(self):
        #类被加载时要创建一个文件
        self.file =open('executive_prep.csv' ,'w',encoding='utf-8')
        self.file.write("高管姓名,性别,年龄,股票代码,职位\n")

    def process_item(self, item, spider):
        self.write_content(item)
        return item

    def write_content(self,item):
        names = item["names"]
        sexes = item["sexes"]
        ages = item["ages"]
        codes = item["codes"]
        leaders = item["leaders"]

        result = ""
        for i in range(len(names)):
            result = names[i] + "," + sexes[i] + "," + ages[i] + "," + codes[0] + "," + leaders[i] + "\n"
            self.file.write(result)
            # print(result)
