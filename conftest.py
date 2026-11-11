import pytest
from selenium import webdriver


@pytest.fixture # фикстуру с yield посоветовал ИИ
def driver():
    driver = webdriver.Chrome() 
    yield driver 
    driver.quit()
