from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPage: 
    url_main_page = "https://qa-desk.education-services.ru/"
    BUTTON_ENTER_AND_REG = [By.XPATH, ".//button[text()='Вход и регистрация']"]
    BUTTON_NO_ACCOUNT = [By.XPATH, ".//button[text()='Нет аккаунта']"]
    INPUT_EMAIL = [By.XPATH, ".//input[@placeholder='Введите Email']"]
    INPUT_PASSWORD = [By.XPATH, ".//input[@placeholder='Пароль']"]
    INPUT_REPEAT_PASSWORD = [By.XPATH, ".//input[@placeholder='Повторите пароль']"]
    BUTTON_CREATE_ACCOUNT = [By.XPATH, ".//button[text()='Создать аккаунт']"]
    USER_NAME = [By.CSS_SELECTOR, "[class='profileText name']"]
    BUTTON_PROFILE = [By.CSS_SELECTOR, "button.circleSmall"]
    ERROR_EMAIL = [By.XPATH, ".//span[text()='Ошибка']"]
    FIELD_EMAIL = [By.XPATH, ".//input[@placeholder='Введите Email']/parent::div"]
    FIELD_PASSWORD = [By.XPATH, ".//input[@placeholder='Пароль']/parent::div"]  
    FIELD_REPEAT_PASSWORD = [By.XPATH, ".//input[@placeholder='Повторите пароль']/parent::div"]
    BUTTON_LOGOUT = [By.XPATH, ".//button[text()='Выйти']"]
    BUTTON_ENTER = [By.XPATH, ".//button[text()='Войти']"]


class CreateAd:
    BUTTON_PLACE_AD = [By.XPATH, ".//button[text()='Разместить объявление']"]
    POPUP_SIGNIN = [By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"]
    NAME = [By.NAME, "name"]
    BUTTON_LIST_OF_CATEGORY = [By.XPATH, ".//input[@name='category']/parent::div/button"]
    CATEGORY_BOOKS = [By.XPATH, ".//span[text()='Книги']/parent::button"]
    BUTTON_LIST_OF_CITY = [By.XPATH, ".//input[@name='city']/parent::div/button"]
    CITY_EKB = [By.XPATH, ".//span[text()='Екатеринбург']/parent::button"]
    SECOND_RADIO_BUTTON = [By.XPATH, ".//label[text()='Б/У']"]
    DESCRIPTION = [By.XPATH, ".//textarea[@placeholder='Описание товара']"]
    PRICE = [By.XPATH, ".//input[@placeholder='Стоимость']"]
    BUTTON_PUBLISH = [By.XPATH, ".//button[text()='Опубликовать']"]
    MY_AD = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div"]
    MY_CARDS = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class = 'card']"]
    CREATING_AD_NAME = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h2"]
    CREATING_AD_CITY = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h3"]
    CREATING_AD_PRICE = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[@class='price']/h2"]
