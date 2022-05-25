from Base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class OzonLocators:

    LOCATOR_LOG_IN_BUTTON = (By.XPATH,"//span[text()='Войти']")

    LOCATOR_ORDERS = (By.XPATH,"//span[text()='Заказы']")

    LOCATOR_FAVOURITES = (By.XPATH,"//span[text()='Избранное']")

    LOCATOR_FAVOURITES = (By.XPATH, "//span[text()='Корзина']")

    LOCATOR_SEARCH = (By.CSS_SELECTOR,"[placeholder='Искать на Ozon']")

    LOCATOR_CATALOG = (By.XPATH,"//span[text()='Каталог']")


class Helper(BasePage):

    def enter_word(self,word):
        search_filed_clear = self.find_element(OzonLocators.LOCATOR_SEARCH).clear() #clear field search
        search_filed_send = self.find_element(OzonLocators.LOCATOR_SEARCH).send_keys(f'{word}'+ Keys.ENTER)
        return search_filed_send

        # search_filed = self.find_element(OzonLocators.LOCATOR_SEARCH).clear()  # clear field search
        # search_filed.send_keys(f'{word}' + Keys.ENTER)
        # return search_filed


    def click_on_button(self,locator):
            return self.find_element(locator).click()


