#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 16:28
# @Author  : xiaohl
import logging


class JsonComparator:
    def __init__(self):
        pass

    def equal(self, live_json, std_json):
        logging.info("live_json " + str(live_json))
        logging.info("std_json " + str(std_json))
        return live_json == std_json

    def less_than(self, live_json, std_json):
        pass

    def more_than(self, live_json, std_json):
        pass