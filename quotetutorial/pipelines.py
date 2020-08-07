# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time


class QuotetutorialPipeline(object):

    def __init__(self):
        self.cred = credentials.Certificate("FIREBASE_CONNECTION_FILE")
        firebase_admin.initialize_app(self.cred, {
            "databaseURL": "FIREBASE_DB_URL"
        })

    def process_item(self, item, spider):
        print("pipeline: ", item['title'])
        unique_key = db.reference('spider').push().key
        db.reference().update({
            'spider/{}'.format(unique_key): dict(item)
        })
        # time.sleep(5)
        return item
