"""
@Time    : 2024/5/6 18:22
@Author  : 王森 
@File    : select_role_page.py
@IDE     : PyCharm
"""
from page.base_page import BasePage
from page.page_locator import RoleLocators
class SelectRolePage(BasePage):
    def select_role(self,role):
        if role=='ot':
            self.click(RoleLocators.ot)
        else:
            self.click(RoleLocators.it)
