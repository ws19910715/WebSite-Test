import pytest
import time
import allure
import os
from utils.ui import *
from utils.config import *
#driver=open()

@allure.feature('点检')
def test(login):
    "创建点检计划"
    driver=login
    driver.click("xpath=>//*[@id='app']/div[1]/div[1]/div/ul/li[5]/span")
    time.sleep(2)
    driver.get_screen_shot(image_path+picture_time+"点检.png")
    with open(image_path+picture_time+"点检.png",mode='rb') as f:
        file=f.read()
        allure.attach(file,'点检')
@allure.feature('新建事件')
def test_event_1(login):
    """
    事件引擎测试用例
    新建事件
    :param login:
    :return:
    """
    driver=login
    el=d['event'][0]
    driver.move_to_element(el['more'])
    driver.click(el['menu'])
    driver.click(el['event'])
    driver.click(el['sjgl'])
    time.sleep(2)
    driver.get_screen_shot(image_path+picture_time+"事件引擎.png",'事件引擎')
    driver.click(el['add_event'])
    driver.send_value(el['event_name'],'ui测试')

if __name__ == "__main__":
    pytest.main(['-s','test.py::test_event_1','--alluredir=report'])
    os.system("allure generate --clean report")