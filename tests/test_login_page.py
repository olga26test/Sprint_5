from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage


class TestLoginPage:
    def test_login(self, driver):
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

        # авторизуемся под созданным аккаунтом
        driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
        driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
        driver.find_element(*RegPage.INPUT_PASSWORD).send_keys("qwertY123$")
        driver.find_element(*RegPage.BUTTON_ENTER).click()
        WebDriverWait(driver, 30).until(EC.visibility_of_element_located((RegPage.USER_NAME)))

        # проверяем, что есть имя User. и аватар    
        assert (driver.find_element(*RegPage.USER_NAME).text == "User.") and (len(driver.find_elements(*RegPage.BUTTON_PROFILE)) == 1)

    def test_logout(self, driver):
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

        # проверяем, что имя User. и аватар отсутствуют и есть кнопка «Вход и регистрация»
        assert len(driver.find_elements(*RegPage.USER_NAME)) == 0 and len(driver.find_elements(*RegPage.BUTTON_PROFILE)) == 0 and len(driver.find_elements(*RegPage.BUTTON_ENTER_AND_REG)) == 1 
    