#!/usr/bin/env python
# -*- coding:utf-8 -*-
# cy

from appium import webdriver

class TestSetting:

    def testset(self):

        desired_caps = {}

        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = '192.168.56.101:5555'
        desired_caps['appPackage'] = 'com.android.settings'
        desired_caps['appActivity'] = '.Settings'
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True

        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)