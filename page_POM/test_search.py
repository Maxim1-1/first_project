import pytest

from Page_object import Helper
from selenium import webdriver


def test_send_keys_search(browser_driver):
    ozon_main_page = Helper(browser_driver)
    ozon_main_page.go_to_site()
    ozon_main_page.enter_word('видеокарты')
    current_url = ozon_main_page.current_url()
    print(current_url)
    assert str(current_url) != 'https://www.ozon.ru/'

