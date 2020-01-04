import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Обработчик, который считывает из командной строки параметр language.
def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default=None, help="Choose language")

#Фикстура логики запуска браузера с указанным языком пользователя
@pytest.fixture() # scope=“function” — дефолтное значение и его можно не указывать
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\n\nStart browser...")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\n\nQuit browser.")
    browser.quit()

