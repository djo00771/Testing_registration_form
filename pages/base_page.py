from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_clickable(self, locator, timeout=5):
        """ Проверить кликабельность элемента """
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def element_is_visible(self, locator, timeout=5):
        """ Видимость элемента """
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=5):
        """ Видимость всех элементов """
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def remove_element(self):
        """ Удалить элемент со страницы """
        self.driver.execute_script("document.getElementsByTagName('footer')[0].remove();")

    def refresh(self):
        """ Обновить страницу """
        self.driver.refresh()

    def get_current_url(self):
        """ Получить адрес текущей страницы. """
        return self.driver.current_url
