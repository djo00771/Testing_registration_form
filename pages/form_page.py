import os
import time
from selenium.webdriver import Keys
from generator.generator import generated_person, generated_file
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_field_and_submit(self):
        """ Заполнить поля и отправить """
        person = generated_person()
        path = generated_file()
        self.remove_element()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECT)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(path)
        os.remove(path)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        return person

    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = [i.text for i in result_list]

        return result_text


