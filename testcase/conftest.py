from utils.ui import *
import time
import pytest
import os
from utils.ui import *
import allure
from utils.config import *
@pytest.fixture()
def login():
    """登录智慧工厂"""
    driver=browser('chrome')
    el=d['loging'][0]
    driver.wait(20)
    driver.open(url)
    driver.max_window()
    driver.send_value(el['user'],pt_user)
    driver.send_value(el['password'],pt_password)
    code=driver.get_text(el['get_code'])
    driver.send_value(el['code'],code)
    driver.get_screen_shot(image_path+picture_time+"登录.png")
    driver.click(el['login'])
    with open(image_path+picture_time+'登录.png' , mode='rb') as f:
        file = f.read()
        allure.attach(file, '登录')
    user=driver.get_text(el['username'])
    with allure.step("登录用户%s"%pt_user):
        assert user==pt_user
    yield driver
    """关闭浏览器"""
    driver.quit()



