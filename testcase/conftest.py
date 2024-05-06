import pytest
import allure
from utils.utils import select_browser,get_now
from config.config import *
from page.login_page import LoginPage
@pytest.fixture(scope='module')
def login():
    """登录"""
    driver =select_browser()
    driver = LoginPage(driver)
    driver.open(URL)
    driver.max_window()
    driver.login(USER,PASSWORD)
    driver.get_screen_shot(IMAGE_PATH+get_now()+"登录.png",'登录')
    yield driver
    """关闭浏览器"""




