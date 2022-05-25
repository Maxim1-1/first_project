from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import pytest
from selenium import webdriver



class BasePage:

    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'https://www.ozon.ru/'

    def find_element(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_element_located(locator),message=f'Cant find element by locator {locator}')


    def find_elements(self,locator,time=10):
        return WebDriverWait(self.driver,time).until(EC.presence_of_all_elements_located(locator),message=f'Cant find element by locator {locator}')


    def go_to_site(self):
        return self.driver.get(self.base_url)

    def move_to_element_action(self):
        self.action = ActionChains(self.driver)
        return self.action

    def screensshots(self,name_scr):
        self.driver.save_schreenshot(f'{name_scr}.png')

    def current_url(self):
        return self.driver.current_url



