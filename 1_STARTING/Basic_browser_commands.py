#pip install selenium #in pycharm terminal
"""

from selenium import webdriver

class Basic_selenium:
    def initialize_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()
x = Basic_selenium()
x.initialize_browser()

#https://selenium.qabible.in/
#***************************************************************************
from selenium import webdriver
class Basic_selenium:
    def initialize_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium.qabible.in/")
        self.driver.maximize_window()

    def close_browser(self):
        self.driver.close()

x = Basic_selenium()
x.initialize_browser()
x.close_browser()
#***************************************************************************
"""
import time
from selenium import webdriver

class Basic_selenium:
    def initialize_browser(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://selenium.qabible.in/")
        time.sleep(1) #make delay by 5 sec
        self.driver.maximize_window()
        time.sleep(5)
    def close_browser(self):
        #self.driver.close()  ##to close the tab in browser
        self.driver.quit() ##to close browser completely
x = Basic_selenium()
x.initialize_browser()
x.close_browser()

#***************************************************************************
#Browser commands :





