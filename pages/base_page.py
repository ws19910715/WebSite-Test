# coding=utf-8
"""
此文件为selenium常用方法二次封装文件
"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
import allure
import re
from utils.utils import get_now
from config.config import IMAGE_PATH

class BasePage:
    """
    Selenium框架的主要类
    """
    original_window = None

    def __init__(self, driver:webdriver):
        """
        初始化BasePage类
        :param driver: WebDriver实例
        """
        self.driver = driver

    def element_wait(self, by, value, secs=10):
        """
        等待元素显示
        :param by: 元素定位方式
        :param value: 元素定位值
        :param secs: 超时时间
        """
        locators = {
            "id": By.ID,
            "name": By.NAME,
            "class": By.CLASS_NAME,
            "link_text": By.LINK_TEXT,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR
        }
        try:
            WebDriverWait(self.driver, secs).until(EC.presence_of_element_located((locators[by], value)))
        except TimeoutException:
            print(f"查找元素超时，请检查元素定位方式 '{by}' 和值 '{value}'")

    def get_element(self, css):
        """
        根据传入的定位方式和值，获取页面元素
        :param css: 元素定位方式和值，格式为"定位方式=>值"
        :return: WebElement对象
        """
        self.driver.implicitly_wait(20)
        # 使用正则表达式检查定位方式和值的格式
        match = re.match(r"^(id|name|class|link_text|xpath|css)=>(.+)$", css)
        if match:
            by = match.group(1)
            value = match.group(2)
            self.element_wait(by, value)
            locators = {
                "id": By.ID,
                "name": By.NAME,
                "class": By.CLASS_NAME,
                "link_text": By.LINK_TEXT,
                "xpath": By.XPATH,
                "css": By.CSS_SELECTOR
            }
            locator = (locators[by], value)
            return self.driver.find_element(*locator)
        else:
            raise ValueError("语法错误，请参考：'id=>kw' 或 'xpath=>//*[@id='kw']'")

    def open(self, url):
        """
        打开url.
        用法:
        driver.open("https://www.baidu.com")
        """
        self.driver.get(url)

    def max_window(self):
        """
        设置浏览器最大化.
        用法:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置浏览器窗口宽和高.
        用法:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)

    def send_value(self, css, text):
        """
        操作输入框.
        用法:
        driver.type("css=>#el","selenium")
        """
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        """
        清除输入框的内容.
        用法:
        driver.clear("css=>#el")
        """
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        """
        它可以点击任何文本/图像
        连接，复选框，单选按钮，甚至下拉框等等..
        用法:
        driver.click("css=>#el")
        """
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        """
        右键单击元素.
        用法:
        driver.right_click("css=>#el")
        """
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        """
        鼠标移到元素（悬停）.
        用法:
        driver.move_to_element("css=>#el")
        """
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        """
        双击元素.
        用法:
        driver.double_click("css=>#el")
        """
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        """
        把一个元素拖到一定的距离，然后把它放下.
        用法:
        driver.drag_and_drop("css=>#el","css=>#ta")
        """
        element = self.get_element(el_css)
        target = self.get_element(ta_css)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        """
        单击链接文本中的元素
        用法:
        driver.click_text("新闻")
        """
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        模拟用户在弹出框的标题栏中点击“关闭”按钮窗口或选项卡.
        Usage:
        driver.close()
        """
        self.driver.close()

    def quit(self):
        """
        关闭使用的所有窗口.
        用法:
        driver.quit()
        """
        self.driver.quit()


    def submit(self, css):
        """
        提交指定的表单
        用法:
        driver.submit("css=>#el")
        """
        el = self.get_element(css)
        el.submit()

    def refresh_page(self):
        """
        刷新当前页面.
        用法:
        driver.F5()
        """
        self.driver.refresh()

    def js(self, script):
        """
        执行JavaScript脚本.
        用法:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        """
        获取元素属性的值.
        用法:
        driver.get_attribute("css=>#el","type")
        """
        el = self.get_element(css)
        return el.get_attribute(attribute)

    def get_text(self, css):
        """
        获得元素文本信息
        用法:
        driver.get_text("css=>#el")
        """
        el = self.get_element(css)
        return el.text

    def get_display(self, css):
        """
        获取元素来显示，返回结果为真或假.
        用法:
        driver.get_display("css=>#el")
        """
        el = self.get_element(css)
        return el.is_displayed()

    def get_title(self):
        """
        得到窗口标题.
        用法:
        driver.get_title()
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前页面的URL地址.
        用法:
        driver.get_url()
        """
        return self.driver.current_url

    def get_alert_text(self):
        """
        得到警报的文本.
        用法:
        driver.get_alert_text()
        """
        return self.driver.switch_to.alert.text

    def wait(self, secs):
        """
        隐式等，页面上的所有元素.
        用法:
        driver.wait(10)
        """
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        接受警告框.
        用法:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        Dismisses the alert available.
        用法:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        """
        切换到指定的frame.
        用法:
        driver.switch_to_frame("css=>#el")
        """
        iframe_el = self.get_element(css)
        self.driver.switch_to.frame(iframe_el)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.
        Usage:
        driver.switch_to_frame_out()
        """
        self.driver.switch_to.default_content()

    def open_new_window(self, css):
        """
        打开新窗口并切换到新打开的窗口.
        用法:
        传入一个点击后会跳转的元素
        driver.open_new_window("link_text=>注册")
        """
        original_window = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_window:
                self.driver.switch_to.window(handle)

    def get_screen_shot(self, bewrite):
        """将当前窗口的屏幕截图保存到PNG图像文件中.
        用法:
        driver.get_screen_shot('/Screenshots/foo.png')
        """
        file_path =IMAGE_PATH + get_now()+bewrite+'.png'
        self.driver.get_screenshot_as_file(file_path)
        with open(file_path,mode='rb')as f:
            file=f.read()
            allure.attach(file,bewrite)
    def fallback(self):
        self.driver.back()

    def select(self, css, value):
        """
        构造函数。对给定的元素进行了检查，确实是一个SELECT标记。如果不是,
        然后抛出一个意料之外的tag name exception.
        :Args:
         - css - element SELECT element to wrap
         - value - The value to match against
        Usage:
            <select name="NR" id="nr">
                <option value="10" selected="">每页显示10条</option>
                <option value="20">每页显示20条</option>
                <option value="50">每页显示50条</option>
            </select>
            driver.select("#nr", '20')
            driver.select("xpath=>//[@name='NR']", '20')
        """
        el = self.get_element(css)
        Select(el).select_by_value(value)


