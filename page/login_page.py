"""
@Time    : 2024/5/6 14:42
@Author  : 王森 
@File    : login_page.py
@IDE     : PyCharm
"""
from page.base_page import BasePage
from page.page_locator import LoginLocators
import allure
class LoginPage(BasePage):
    @allure.step(f'用户登录')
    def login(self,username,password):
        self.send_value(LoginLocators.username,username)
        self.send_value(LoginLocators.password,password)
        self.click(LoginLocators.login_button)

    def get_login_message(self):
       return self.get_text(LoginLocators.login_success)