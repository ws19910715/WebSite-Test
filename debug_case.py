"""
@Time    : 2024/5/8 13:20
@Author  : 王森 
@File    : debug_case.py
@IDE     : PyCharm
"""
from utils.utils import remove_folders
import os
if __name__ == '__main__':
    remove_folders('./report')
    remove_folders('./allure-report')
    os.system(r' pytest -s -q .\tests\ --alluredir=report')
    os.system(r'allure generate .\report\ -o allure-report')