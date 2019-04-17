#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 14:16
# @Author  : xiaohl
import random
import string
import time


def update_json_value_by_key(json_obj, key, new_value):
    json_obj[key] = new_value
    return json_obj

def get_timestamp_value(value):
    return value + "_" + time.strftime("%Y%m%d%H%M%S")

def get_random_mobile():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    return "".join(random.choice(prelist)) + "".join(random.choice("0123456789") for i in range(8))

def get_random_string(length = 5):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    all_string = lowercase + uppercase + "0123456789"
    # print(all_string)
    return "".join(random.choice(all_string) for i in range(length))

if __name__ == "__main__":
    print(get_timestamp_value("账单"))
    print(get_random_mobile())
    print(get_random_char())