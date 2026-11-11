from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage, CreateAd


def test_create_ad_unauth_user(driver):
    driver.get("https://qa-desk.education-services.ru/")

    # пытаемся создать объявление неавторизованным пользователем
    driver.find_element(By.XPATH, CreateAd.button_place_ad).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, CreateAd.popup_signin)))

    # проверяем, что появляется модалка с заголовком «Чтобы разместить объявление, авторизуйтесь»
    assert len(driver.find_elements(By.XPATH, CreateAd.popup_signin)) == 1 and driver.find_element(By.XPATH, CreateAd.popup_signin).text == "Чтобы разместить объявление, авторизуйтесь"


def test_create_ad_auth_user(driver):
    driver.get("https://qa-desk.education-services.ru/")

    # создаем аккаунт
    driver.find_element(By.XPATH, RegPage.button_enter_and_reg).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.button_no_account)))
    driver.find_element(By.XPATH, RegPage.button_no_account).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, RegPage.input_email)))
    email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
    driver.find_element(By.XPATH, RegPage.input_email).send_keys(email_random)
    driver.find_element(By.XPATH, RegPage.input_password).send_keys("12345")
    driver.find_element(By.XPATH, RegPage.input_repeat_password).send_keys("12345")
    driver.find_element(By.XPATH, RegPage.button_create_account).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, RegPage.user_name)))
    
    # размещаем объявление
    driver.find_element(By.XPATH, CreateAd.button_place_ad).click()
    driver.find_element(By.NAME, CreateAd.name).send_keys("Трудно быть богом")
    driver.find_element(By.XPATH, CreateAd.button_list_of_category).click()
    driver.find_element(By.XPATH, CreateAd.category_books).click()
    driver.find_element(By.XPATH, CreateAd.button_list_of_city).click()
    driver.find_element(By.XPATH, CreateAd.city_ekb).click()
    driver.find_element(By.XPATH, CreateAd.second_radio_button).click()
    driver.find_element(By.XPATH, CreateAd.description).send_keys("Продаю книгу «Трудно быть богом» в хорошем состоянии")
    driver.find_element(By.XPATH, CreateAd.price).send_keys(650)
    driver.find_element(By.XPATH, CreateAd.button_publish).click()
    WebDriverWait(driver, 15).until(EC.url_to_be("https://qa-desk.education-services.ru/"))

    # переходим в профиль пользователя
    driver.find_element(By.CSS_SELECTOR, RegPage.button_profile).click()
    WebDriverWait(driver, 10).until(EC.url_contains("profile")) 
    block_my_ad = driver.find_element(By.XPATH, CreateAd.my_ad)
    driver.execute_script("arguments[0].scrollIntoView();", block_my_ad)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, CreateAd.creating_ad_name)))

    # проверяем, что есть карточка созданного объявления с верным названием, городом и ценой
    assert len(driver.find_elements(By.XPATH, CreateAd.my_cards)) == 1 and driver.find_element(By.XPATH, CreateAd.creating_ad_name).text == "Трудно быть богом" and driver.find_element(By.XPATH, CreateAd.creating_ad_city).text == "Екатеринбург" and driver.find_element(By.XPATH, CreateAd.creating_ad_price).text == "650 ₽"
  