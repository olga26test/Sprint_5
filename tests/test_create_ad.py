from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import random as r
from locators import RegPage, CreateAd


def test_create_ad_unauth_user(driver):
    driver.get(RegPage.url_main_page)

    # пытаемся создать объявление неавторизованным пользователем
    driver.find_element(*CreateAd.BUTTON_PLACE_AD).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((CreateAd.POPUP_SIGNIN)))

    # проверяем, что появляется модалка с заголовком «Чтобы разместить объявление, авторизуйтесь»
    assert len(driver.find_elements(*CreateAd.POPUP_SIGNIN)) == 1 and driver.find_element(*CreateAd.POPUP_SIGNIN).text == "Чтобы разместить объявление, авторизуйтесь"


def test_create_ad_auth_user(driver):
    driver.get(RegPage.url_main_page)

    # создаем аккаунт
    driver.find_element(*RegPage.BUTTON_ENTER_AND_REG).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.BUTTON_NO_ACCOUNT)))
    driver.find_element(*RegPage.BUTTON_NO_ACCOUNT).click()
    WebDriverWait(driver, 3).until(EC.visibility_of_element_located((RegPage.INPUT_EMAIL)))
    email_random = f"olya{r.randint(10000, 999999)}@gmail.com"
    driver.find_element(*RegPage.INPUT_EMAIL).send_keys(email_random)
    driver.find_element(*RegPage.INPUT_PASSWORD).send_keys("12345")
    driver.find_element(*RegPage.INPUT_REPEAT_PASSWORD).send_keys("12345")
    driver.find_element(*RegPage.BUTTON_CREATE_ACCOUNT).click()
    WebDriverWait(driver, 30).until(EC.visibility_of_element_located((RegPage.USER_NAME)))
    
    # размещаем объявление
    driver.find_element(*CreateAd.BUTTON_PLACE_AD).click()
    driver.find_element(*CreateAd.NAME).send_keys("Трудно быть богом")
    driver.find_element(*CreateAd.BUTTON_LIST_OF_CATEGORY).click()
    driver.find_element(*CreateAd.CATEGORY_BOOKS).click()
    driver.find_element(*CreateAd.BUTTON_LIST_OF_CITY).click()
    driver.find_element(*CreateAd.CITY_EKB).click()
    driver.find_element(*CreateAd.SECOND_RADIO_BUTTON).click()
    driver.find_element(*CreateAd.DESCRIPTION).send_keys("Продаю книгу «Трудно быть богом» в хорошем состоянии")
    driver.find_element(*CreateAd.PRICE).send_keys(650)
    driver.find_element(*CreateAd.BUTTON_PUBLISH).click()
    WebDriverWait(driver, 15).until(EC.url_to_be(RegPage.url_main_page))

    # переходим в профиль пользователя
    driver.find_element(*RegPage.BUTTON_PROFILE).click()
    WebDriverWait(driver, 10).until(EC.url_contains("profile")) 
    block_my_ad = driver.find_element(*CreateAd.MY_AD)
    driver.execute_script("arguments[0].scrollIntoView();", block_my_ad)
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((CreateAd.CREATING_AD_NAME)))

    # проверяем, что есть карточка созданного объявления с верным названием, городом и ценой
    assert len(driver.find_elements(*CreateAd.MY_CARDS)) == 1 and driver.find_element(*CreateAd.CREATING_AD_NAME).text == "Трудно быть богом" and driver.find_element(*CreateAd.CREATING_AD_CITY).text == "Екатеринбург" and driver.find_element(*CreateAd.CREATING_AD_PRICE).text == "650 ₽"
  