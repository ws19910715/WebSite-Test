"""
@Time    : 2024/5/6 14:42
@Author  : 王森 
@File    : login_page.py
@IDE     : PyCharm
"""


from pages.base_page import BasePage
from pages_elements.login_elements import LoginElements
import allure
class LoginPage(BasePage):
    @allure.step(f'用户登录')
    def login(self,username,password):
        self.send_value(LoginElements.username, username)
        self.send_value(LoginElements.password, password)
        self.click(LoginElements.login_button)

    @allure.step(f'获取登录信息')
    def get_login_message(self):
       return self.get_text(LoginElements.login_message)