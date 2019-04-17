#! /usr/bin/env python
#coding=utf-8
import logging
from src.apis.baseapi import BaseAPI
from src.initialization.sysconfig import sys_cfg
import time
class DeptManagment(BaseAPI):

    def __init__(self):
        BaseAPI.__init__(self)
        logging.info("Init department management API")
        self.create_dep_url = sys_cfg.get('contact_para', 'create_dep_url')
        self.dep_secure = sys_cfg.get('contact_para', 'secure')


    def create_dept(self):
        name = "接口自动化"+time.strftime("%y%m%d%%S")
        new_part = {
           "name": name,
           "parentid": 1,
           # "order": 1
        }
        param = {'access_token': self.get_token(self.dep_secure)}

        logging.debug("url:"+str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url, new_part, params=param)

    def get_create_dept_res(self):
        return self.get_response()

    def create_dept_by_para(self,name):
        new_part={
       "name": name,
       "parentid": 1,
       "order": 1
        }

        param = {'access_token':self.get_token(self.dep_secure)}
        logging.debug("url:"+str(self.create_dep_url))
        logging.debug("params:" + str(param))
        self.post_json(self.create_dep_url,new_part,params=param)

