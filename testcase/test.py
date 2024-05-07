import time

import allure
import pytest
from config.config import *
from page.login_page import LoginPage
from page.select_role_page import SelectRolePage
from page.base_page import BasePage
from utils.utils import select_browser,get_now
class Test_Iot:
    def setup_class(self):
        driver = select_browser()
        self.driver = driver
        base_page = BasePage(driver)
        base_page.max_window()
        base_page.open(URL)

    def teardown_class(self):
        self.driver.quit()
    @allure.title('登录测试')
    def test_login(self):
        driver = LoginPage(self.driver)
        driver.login(USER,PASSWORD)
        time.sleep(2)
        login_png = IMAGE_PATH + get_now() + "登录.png"
        driver.get_screen_shot(login_png, '登录')
        assert driver.get_login_message()=='登录成功'

    @allure.title('选择OT角色')
    def test_select_role(self):
        driver = SelectRolePage(self.driver)
        driver.select_role('ot')

if __name__ == "__main__":
    pytest.main(['-s','-q','test.py','--alluredir=report'])
    os.system("allure generate --clean report")