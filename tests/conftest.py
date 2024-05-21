import pytest
import allure
from utils.utils import select_browser
from config.config import *
from pages.login_page import LoginPage
from pages.select_role_page import SelectRolePage

@allure.step('打开浏览器并登录')
@pytest.fixture(scope="session")
def login():
    driver = select_browser('chrome_headless')
    login_page = LoginPage(driver)
    login_page.open(URL)
    login_page.max_window()
    login_page.login(USER, PASSWORD)
    login_page.get_screen_shot('登录')
    SelectRolePage(driver).select_role('ot')
    yield driver
    login_page.quit()


@pytest.fixture(scope="function", autouse=True)
@allure.step('检查登录状态')
def if_login(login):
    if login.current_url==URL:
        login_page = LoginPage(login)
        login_page.refresh_page()
        login_page.login(USER, PASSWORD)
        SelectRolePage(login).select_role('ot')



