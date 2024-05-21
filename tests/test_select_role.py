"""
@Time    : 2024/5/7 17:19
@Author  : 王森 
@File    : test_select_role.py
@IDE     : PyCharm
"""
import time
import allure
import pytest
from pages.select_role_page import SelectRolePage

class Test_select_role:
    @pytest.fixture(autouse=True)
    def _setup_class(self, login):
        self.driver = SelectRolePage(login)

    @allure.title('选择OT角色')
    def test_select_role_oT(self):
        self.driver.remove_role()
        self.driver.select_role('ot')
        time.sleep(3)
        self.driver.get_screen_shot('选择OT角色')
        assert self.driver.get_role_name()=='OT'