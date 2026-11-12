from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPage: 
    url_main_page = "https://qa-desk.education-services.ru/"
    button_enter_and_reg = [By.XPATH, ".//button[text()='Вход и регистрация']"]
    button_no_account = [By.XPATH, ".//button[text()='Нет аккаунта']"]
    input_email = [By.XPATH, ".//input[@placeholder='Введите Email']"]
    input_password = [By.XPATH, ".//input[@placeholder='Пароль']"]
    input_repeat_password = [By.XPATH, ".//input[@placeholder='Повторите пароль']"]
    button_create_account = [By.XPATH, ".//button[text()='Создать аккаунт']"]
    user_name = [By.CSS_SELECTOR, "[class='profileText name']"]
    button_profile = [By.CSS_SELECTOR, "button.circleSmall"]
    error_email = [By.XPATH, ".//span[text()='Ошибка']"]
    field_email = [By.XPATH, ".//input[@placeholder='Введите Email']/parent::div"]
    field_password = [By.XPATH, ".//input[@placeholder='Пароль']/parent::div"]  
    field_repeat_password = [By.XPATH, ".//input[@placeholder='Повторите пароль']/parent::div"]
    button_logout = [By.XPATH, ".//button[text()='Выйти']"]
    button_enter = [By.XPATH, ".//button[text()='Войти']"]


class CreateAd:
    button_place_ad = [By.XPATH, ".//button[text()='Разместить объявление']"]
    popup_signin = [By.XPATH, ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"]
    name = [By.NAME, "name"]
    button_list_of_category = [By.XPATH, ".//input[@name='category']/parent::div/button"]
    category_books = [By.XPATH, ".//span[text()='Книги']/parent::button"]
    button_list_of_city = [By.XPATH, ".//input[@name='city']/parent::div/button"]
    city_ekb = [By.XPATH, ".//span[text()='Екатеринбург']/parent::button"]
    second_radio_button = [By.XPATH, ".//label[text()='Б/У']"]
    description = [By.XPATH, ".//textarea[@placeholder='Описание товара']"]
    price = [By.XPATH, ".//input[@placeholder='Стоимость']"]
    button_publish = [By.XPATH, ".//button[text()='Опубликовать']"]
    my_ad = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div"]
    my_cards = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class = 'card']"]
    creating_ad_name = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h2"]
    creating_ad_city = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h3"]
    creating_ad_price = [By.XPATH, ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[@class='price']/h2"]
