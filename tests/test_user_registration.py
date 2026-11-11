from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage


def test_registration(driver):
    driver.get("https://qa-desk.education-services.ru/")

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

    # проверяем, что есть имя User. и аватар    
    assert (driver.find_element(By.CSS_SELECTOR, RegPage.user_name).text == "User.") and (len(driver.find_elements(By.CSS_SELECTOR, RegPage.button_profile)) == 1)


def test_registration_with_invalid_mask_email(driver):
    driver.get("https://qa-desk.education-services.ru/")

    # пытаемся зарегистрироваться с невалидным email
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_no_account)))
    driver.find_element(By.XPATH, RegPage.button_no_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    email_random = f"olya{r.randint(10000, 999999)}gmailcom"
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.button_create_account).click()

    # ожидаем, чтобы успел появиться элемент с текстом Ошибка
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.error_email)))

    # находим border каждого поля
    field_email_border_color = driver.find_element(By.XPATH, RegPage.field_email).value_of_css_property("border-color")
    field_password_border_color = driver.find_element(By.XPATH, RegPage.field_password).value_of_css_property("border-color")
    field_repeat_password_border_color = driver.find_element(By.XPATH, RegPage.field_repeat_password).value_of_css_property("border-color")

    # проверяем наличие текста Ошибка под полем Email, и что все 3 поля выделены красным цветом
    assert len(driver.find_elements(By.XPATH, RegPage.error_email)) == 1 and field_email_border_color == "rgb(255, 105, 114)" and field_password_border_color == "rgb(255, 105, 114)" and field_repeat_password_border_color == "rgb(255, 105, 114)"


def test_registration_existing_user(driver):
    driver.get("https://qa-desk.education-services.ru/")

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

    # пытаемся зарегистрироваться под только что созданным юзером
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_no_account)))
    driver.find_element(By.XPATH, RegPage.button_no_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.input_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.input_repeat_password).send_keys("qwertY123$")
    driver.find_element(By.XPATH, RegPage.button_create_account).click()

    # ожидаем, чтобы успел появиться элемент с текстом Ошибка
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.error_email)))

    # находим border каждого поля
    field_email_border_color = driver.find_element(By.XPATH, RegPage.field_email).value_of_css_property("border-color")
    field_password_border_color = driver.find_element(By.XPATH, RegPage.field_password).value_of_css_property("border-color")
    field_repeat_password_border_color = driver.find_element(By.XPATH, RegPage.field_repeat_password).value_of_css_property("border-color")
    
    # проверяем наличие текста Ошибка под полем Email, и что все 3 поля выделены красным цветом
    assert len(driver.find_elements(By.XPATH, RegPage.error_email)) == 1 and field_email_border_color == "rgb(255, 105, 114)" and field_password_border_color == "rgb(255, 105, 114)" and field_repeat_password_border_color == "rgb(255, 105, 114)"
    