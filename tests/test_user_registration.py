from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage


class TestUserRegistration:
    def test_registration(self, driver):
        driver.get(RegPage.url_main_page)

        # создаем аккаунт
        driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.BUTTON_NO_ACCOUNT)))
        driver.find_element(*RegPage.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
        email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.INPUT_REPEAT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.BUTTON_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((RegPage.USER_NAME)))

        # проверяем, что есть имя User. и аватар    
        assert (driver.find_element(*RegPage.USER_NAME).text == "User.") and (len(driver.find_elements(*RegPage.BUTTON_PROFILE)) == 1)


    def test_registration_with_invalid_mask_email(self, driver):
        driver.get(RegPage.url_main_page)

        # пытаемся зарегистрироваться с невалидным email
        driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.BUTTON_NO_ACCOUNT)))
        driver.find_element(*RegPage.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
        email_random = f"olya{r.randint(10000, 999999)}gmailcom"
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
        driver.find_element(*RegPage.BUTTON_CREATE_ACCOUNT).click()

        # ожидаем, чтобы успел появиться элемент с текстом Ошибка
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.ERROR_EMAIL)))

        # находим border каждого поля
        field_email_border_color = driver.find_element(*RegPage.FIELD_EMAIL).value_of_css_property("border-color")
        field_password_border_color = driver.find_element(*RegPage.FIELD_PASSWORD).value_of_css_property("border-color")
        field_repeat_password_border_color = driver.find_element(*RegPage.FIELD_REPEAT_PASSWORD).value_of_css_property("border-color")

        # проверяем наличие текста Ошибка под полем Email, и что все 3 поля выделены красным цветом
        assert len(driver.find_elements(*RegPage.ERROR_EMAIL)) == 1 and field_email_border_color == "rgb(255, 105, 114)" and field_password_border_color == "rgb(255, 105, 114)" and field_repeat_password_border_color == "rgb(255, 105, 114)"


    def test_registration_existing_user(self, driver):
        driver.get(RegPage.url_main_page)

        # создаем аккаунт
        driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.BUTTON_NO_ACCOUNT)))
        driver.find_element(*RegPage.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
        email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.INPUT_REPEAT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.BUTTON_CREATE_ACCOUNT).click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((RegPage.USER_NAME)))

        # выходим из аккаунта
        driver.find_element(*RegPage.BUTTON_LOGOUT).click() 
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((RegPage.BUTTON_ENTER_AND_REG)))

        # пытаемся зарегистрироваться под только что созданным юзером
        driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.BUTTON_NO_ACCOUNT)))
        driver.find_element(*RegPage.BUTTON_NO_ACCOUNT).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.INPUT_REPEAT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.BUTTON_CREATE_ACCOUNT).click()

        # ожидаем, чтобы успел появиться элемент с текстом Ошибка
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.ERROR_EMAIL)))

        # находим border каждого поля
        field_email_border_color = driver.find_element(*RegPage.FIELD_EMAIL).value_of_css_property("border-color")
        field_password_border_color = driver.find_element(*RegPage.FIELD_PASSWORD).value_of_css_property("border-color")
        field_repeat_password_border_color = driver.find_element(*RegPage.FIELD_REPEAT_PASSWORD).value_of_css_property("border-color")
    
        # проверяем наличие текста Ошибка под полем Email, и что все 3 поля выделены красным цветом
        assert len(driver.find_elements(*RegPage.ERROR_EMAIL)) == 1 and field_email_border_color == "rgb(255, 105, 114)" and field_password_border_color == "rgb(255, 105, 114)" and field_repeat_password_border_color == "rgb(255, 105, 114)"
    