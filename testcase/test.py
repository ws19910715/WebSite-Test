import time

import pytest
from config.config import *
from page.login_page import LoginPage
from utils.utils import select_browser,get_now
class Test_Iot:
    def setup_class(self):
        driver = select_browser()
        self.driver = driver

    def teardown_class(self):
        self.driver.quit()
    def test_login(self):
        driver = LoginPage(self.driver)
        driver.max_window()
        driver.open(URL)
        driver.login(USER,PASSWORD)
        time.sleep(2)
        driver.get_screen_shot(IMAGE_PATH + get_now() + "登录.png", '登录')

if __name__ == "__main__":
    pytest.main(['-s','-q','test.py::test_event_1','--alluredir=report'])
    os.system("allure generate --clean report")