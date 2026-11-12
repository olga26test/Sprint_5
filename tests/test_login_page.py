from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage


def test_login(driver):
    driver.get(RegPage.url_main_page)
    
    # создаем аккаунт
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_no_account)))
    driver.find_element(By.XPATH, RegPage.button_no_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.input_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.input_repeat_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.button_create_account).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, RegPage.user_name)))

    # выходим из аккаунта
    driver.find_element(By.XPATH, RegPage.button_logout).click() 
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_enter_and_reg)))

    # авторизуемся под созданным аккаунтом
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.input_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.button_enter).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, RegPage.user_name)))

    # проверяем, что есть имя User. и аватар    
    assert (driver.find_element(By.CSS_SELECTOR, RegPage.user_name).text == "User.") and (len(driver.find_elements(By.CSS_SELECTOR, RegPage.button_profile)) == 1)

def test_logout(driver):
    driver.get(RegPage.url_main_page)

    # создаем аккаунт
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_no_account)))
    driver.find_element(By.XPATH, RegPage.button_no_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.input_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.input_repeat_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.button_create_account).click() # создаем аккаунт
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, RegPage.user_name)))

    # выходим из аккаунта
    driver.find_element(By.XPATH, RegPage.button_logout).click() 
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_enter_and_reg)))

    # проверяем, что имя User. и аватар отсутствуют и есть кнопка «Вход и регистрация»
    assert len(driver.find_elements(By.CSS_SELECTOR, RegPage.user_name)) == 0 and len(driver.find_elements(By.CSS_SELECTOR, RegPage.button_profile)) == 0 and len(driver.find_elements(By.XPATH, RegPage.button_enter_and_reg)) == 1 
    