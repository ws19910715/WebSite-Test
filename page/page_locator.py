"""
@Time    : 2024/5/6 16:30
@Author  : 王森 
@File    : page_locator.py
@IDE     : PyCharm
"""
class LoginLocators:
    """
    登录页面元素
    """
    username = 'xpath=>//*[@id="ziyun-container"]/div/div[1]/div/div/div[3]/div[3]/span/input'
    password = 'xpath=>//*[@id="ziyun-container"]/div/div[1]/div/div/div[3]/div[4]/span/input'
    login_button = 'xpath=>//*[@id="ziyun-container"]/div/div[1]/div/div/div[3]/button'