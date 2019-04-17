#! /usr/bin/env python
#coding=utf-8

from src.apis.contact.member.membermanagment import MemberManagment
import pytest

class TestCreateMember:

    def test_create_new_member(self):
        member_managment = MemberManagment()
        member_managment.create_member('../testdata/member.json')
        create_res = member_managment.get_response()
        assert create_res.get('errmsg')=='created'

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
