#! /usr/bin/env python
#coding=utf-8

from src.apis.contact.department.depmanagment import DeptManagment
import pytest

class TestCreateDep:

    def test_create_new_dep(self):
        dept_managment = DeptManagment()
        dept_managment.create_dept()
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg') == 'created'

    @pytest.mark.parametrize("name", ["测试部门","产品部门","财务部"])
    def test_create_new_dep_by_para(self,name):
        dept_managment = DeptManagment()
        dept_managment.create_dept_by_para(name)
        create_res = dept_managment.get_response()
        assert create_res.get('errmsg')=='created'
