import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time


class CheckProxy:
    def __init__(self):
        self.driver = webdriver.Chrome().get()

    def __get_url(self):
        self.driver.get(
            'https://b2c.passport.rt.ru/auth/realms/b2c/login-actions/reset-credentials?execution=1b1825d2-f76f-4706-8e25-4c71c1f7f120&client_id=lk_b2c&tab_id=u114Qdv50lU')


    def check_proxy(self):
        self.__get_url()
        time.sleep(100)
