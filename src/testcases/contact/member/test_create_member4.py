#! /usr/bin/env python
#coding=utf-8
import codecs
import json
import logging

from src.apis.contact.member.membermanagment import MemberManagment
from src.untils import tooskit, comparator
import pytest

#此测试用例，测试数据通过类名获取
class TestCreateMember4:

    def test_create_new_member(self):
        member_managment = MemberManagment()
        # file_name = '../testdata/member3.json'
        class_name = self.__class__.__name__
        json_object = member_managment.get_member_file_info('../testdata/' + class_name + '.json')
        for key in json_object:
            case_json_object = member_managment.get_new_member_by_json(json_object, key)
            logging.debug("case_json_object" + str(case_json_object))
            '''
            数据的动态变化
            '''
            new_value = tooskit.get_timestamp_value(case_json_object.get("userid"))
            new_mobile = tooskit.get_random_mobile()
            new_email = tooskit.get_random_string(9) + "@" + case_json_object.get("email").split("@")[1]
            tooskit.update_json_value_by_key(case_json_object, "userid", new_value)
            tooskit.update_json_value_by_key(case_json_object, "mobile", new_mobile)
            tooskit.update_json_value_by_key(case_json_object, "email", new_email)

            member_managment.create_member_by_json(case_json_object)

            create_res = member_managment.get_response()
            # stand_res = json_object.get(key).get("res")
            stand_res = member_managment.get_new_member_by_json(json_object, key, "res")
            json_comparator = comparator.JsonComparator()


            assert json_comparator.equal(create_res, stand_res)

    #此代码无法执行，因为没有对应json文件
    #pip install datafiles
    # @pytest.mark.datafiles(
    #     '../testdata/test1.json',
    #     '../testdata/test2.json',
    #     '../testdata/test3.json')
    # def test_create_new_member(self,datafiles):
    #     for member_file in datafiles.listdir():
    #         member_managment = MemberManagment()
    #         member_managment.create_member(member_file)
    #         create_res = member_managment.get_response()
    #         assert create_res.get('errmsg')=='created'
