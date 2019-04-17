#! /usr/bin/env python
#coding=utf-8

import configparser
import os


def read_config(cfg_file):
    cfg = configparser.ConfigParser()
    if os.path.isfile(cfg_file):
        cfg.read(cfg_file, encoding="utf-8")
        print(os.getcwd())
        return cfg
    else:
        print(cfg_file + " is not exit")



sys_cfg = read_config('C:/Users/admin/Desktop/线上八期接口系列/线上八期接口系列/0331corweixindemo/corweixindemo/cfg/auto.cfg')
# sys_cfg = read_config('../../cfg/auto.cfg')

if __name__=="__main__":
    cfg=read_config("../../cfg/auto.cfg")
    print(cfg.get('contact_para','create_dep_url'))
    create_dep_url = sys_cfg.get('contact_para', 'create_dep_url')
    print(create_dep_url)
