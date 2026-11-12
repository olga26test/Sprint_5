from selenium import webdriver
from selenium.webdriver.common.by import By


class RegPage: 
    url_main_page = "https://qa-desk.education-services.ru/"
    button_enter_and_reg = ".//button[text()='Вход и регистрация']"
    button_no_account = ".//button[text()='Нет аккаунта']"
    input_email = ".//input[@placeholder='Введите Email']"
    input_password = ".//input[@placeholder='Пароль']"
    input_repeat_password = ".//input[@placeholder='Повторите пароль']"
    button_create_account = ".//button[text()='Создать аккаунт']"
    user_name = "[class='profileText name']"
    button_profile = "button.circleSmall"
    error_email = ".//span[text()='Ошибка']"
    field_email = ".//input[@placeholder='Введите Email']/parent::div"
    field_password = ".//input[@placeholder='Пароль']/parent::div"   
    field_repeat_password = ".//input[@placeholder='Повторите пароль']/parent::div"
    button_logout = ".//button[text()='Выйти']"
    button_enter = ".//button[text()='Войти']"


class CreateAd:
    button_place_ad = ".//button[text()='Разместить объявление']"
    popup_signin = ".//h1[text()='Чтобы разместить объявление, авторизуйтесь']"
    name = "name"
    category = "category"
    button_list_of_category = ".//input[@name='category']/parent::div/button"
    category_books = ".//span[text()='Книги']/parent::button"
    button_list_of_city = ".//input[@name='city']/parent::div/button"
    city_ekb = ".//span[text()='Екатеринбург']/parent::button"
    second_radio_button = ".//label[text()='Б/У']"
    description = ".//textarea[@placeholder='Описание товара']"
    price = ".//input[@placeholder='Стоимость']"
    button_publish = ".//button[text()='Опубликовать']"
    my_ad = ".//h1[text()='Мои объявления']/parent::div"
    my_cards = ".//h1[text()='Мои объявления']/parent::div//div[@class = 'card']"
    creating_ad_name = ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h2"
    creating_ad_city = ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[(@class='about')]/h3"
    creating_ad_price = ".//h1[text()='Мои объявления']/parent::div//div[@class='card']//div[@class='price']/h2"
