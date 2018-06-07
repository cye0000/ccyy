#!/usr/bin/env python
# -*- coding:utf-8 -*-
# cy
import allure,pytest

class TestAllure:
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="测试步骤-登录")
    def test_login(self):
        allure.attach('输入名字','输入用户名的描述')
        print('输入名字')
        allure.attach('输入密码', '输入密码的描述')
        print('输入密码')
        allure.attach('点击登录', '输入登录的描述')
        print('点击登录')
        assert 1

    @allure.step(title="测试步骤-登录")
    def test_login01(self):
        print ('111111')
        assert 1

    @allure.step(title="测试步骤-用户名")
    def test_username(self):
        print ('222222')
        assert 1

    @allure.step(title="测试步骤-密码")
    def test_password(self):
        print ('333333')
        assert 0
