"""
@Time    : 2024/5/6 14:24
@Author  : 王森 
@File    : utils.py
@IDE     : PyCharm
"""
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
def select_browser(browser='chrome'):
    if browser == "firefox" or browser == "ff":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "internet explorer" or browser == "ie":
        driver = webdriver.Ie()
    elif browser == "chrome_headless":
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=chrome_options)
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        raise NameError(
            f"找不到 {browser}浏览器,你应该从这里面选取一个 'ie', 'firefox', 'opera', 'edge', 'chrome' or 'chrome_headless'." )
    return driver

def get_now():
    return time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))


def remove_folders(path):
    """
    删除指定目录下的 Allure 报告文件夹。
    """
    try:
        shutil.rmtree(path)
        print(f'成功删除目录：{path}')
    except FileNotFoundError:
        print(f'目录不存在：{path}')
    except Exception as e:
        print(f'删除目录时出错：{e}')