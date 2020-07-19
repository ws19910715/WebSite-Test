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
@allure.title('新建事件')
@allure.severity('top1')
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
    with allure.step('新建事件'):
        driver.send_value(el['event_name'],'ui测试')
        print('事件名称为：ui测试')
        driver.click(el['Push_content'])
        time.sleep(3)
    driver.click(el['xzts'])
    driver.click(el['add_dx'])
    driver.click(el['xzdx'])
    driver.click(el['bc'])
    driver.click(el['add_tsdx'])
    driver.click(el['xzry'])
    driver.click(el['gxry'])
    driver.click(el['gb'])
    driver.click(el['tjtj'])
    time.sleep(2)
    driver.get_screen_shot(image_path+picture_time+".png",'新建事件')
    time.sleep(2)
    driver.click(el['qr'])
    time.sleep(2)
    driver.get_screen_shot(image_path+picture_time+".png",'事件列表')
    event_name=driver.get_text(el['sjmc'])
    if event_name=='ui测试':
        driver.click(el['del_sj'])
        driver.click(el['qr_del'])
        print('第一个事件名称：%s'%event_name)
    else:
        print('第一个事件名称：%s'%event_name)
if __name__ == "__main__":
    pytest.main(['-s','-q','test.py::test_event_1','--alluredir=report'])
    os.system("allure generate --clean report")