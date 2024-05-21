import time
import allure
import pytest
from config.config import *
from pages.login_page import LoginPage




class Test_Login:
    @pytest.fixture( autouse=True)
    def _setup_class(self,login):
        self.driver = LoginPage(login)

    @allure.title('登录测试')
    def test_login(self):
        self.driver.open(URL)
        self.driver.login(USER,PASSWORD)
        time.sleep(2)
        self.driver.get_screen_shot('登录')
        assert self.driver.get_login_message()=='登录成功'

    @allure.title('不存在的用户登录')
    def test_erro_user_login(self):
        self.driver.open(URL)
        self.driver.login('kkkuu',PASSWORD)
        time.sleep(2)
        self.driver.get_screen_shot('不存在的用户登录')
        assert self.driver.get_login_message()=='帐户：kkkuu不存在或状态异常'




if __name__ == "__main__":
    pytest.main(['-s','-q','test_login.py','--alluredir=../report'])
    os.system("allure generate --clean ../report")