"""
@Time    : 2024/5/6 18:22
@Author  : 王森 
@File    : select_role_page.py
@IDE     : PyCharm
"""
from pages.base_page import BasePage
from pages_elements.role_elements import RoleElements
import allure
class SelectRolePage(BasePage):

    @allure.step('选择角色')
    def select_role(self,role):
        if role=='ot':
            self.click(RoleElements.ot)
        else:
            self.click(RoleElements.it)

    @allure.step('获取角色名称')
    def get_role_name(self):
        return self.get_text(RoleElements.role_name)

    @allure.step('移除选择角色并回退到选择角色页面')
    def remove_role(self):
        self.js("localStorage.removeItem('userRole')")
        self.fallback()