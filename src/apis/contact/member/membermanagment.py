#! /usr/bin/env python
#coding=utf-8
import logging
from src.apis.baseapi import BaseAPI
from src.initialization.sysconfig import sys_cfg
import time
import codecs
import json

class MemberManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init member management API")
        self.create_member_url = sys_cfg.get('contact_para', 'create_member_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')


    def get_new_member(self,file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            json_object = json.loads(f.read(), encoding='utf8')
            logging.debug('json_object'+str(json_object))
            return json_object


    def create_member(self,file_name):
        new_member = self.get_new_member(file_name)

        param = {'access_token': self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_member_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_member_url, new_member, params=param)


    # def get_case_object(self, file_name):
    #     with codecs.open(file_name, 'r', encoding='utf8') as f:
    #         multiple_json_object = json.loads(f.read(), encoding='utf8')
    #         case_object = multiple_json_object.get()
    #         logging.debug('case_object' + str(case_object))
    #         return case_object

    def get_member_file_info(self, file_name):
        with codecs.open(file_name, 'r', encoding='utf8') as f:
            file_json_object = json.loads(f.read(), encoding='utf8')
            logging.debug("******************json_object" + str(file_json_object))
            return file_json_object

    def get_new_member_by_json(self, json_object, key,type='req'):
        case_key = json_object.get(key).get(type)
        return case_key

    def create_member_by_json(self, case_json_object):
        param = {'access_token': self.get_token(self.dep_secure)}

        self.post_json(self.create_member_url, case_json_object, params=param)
