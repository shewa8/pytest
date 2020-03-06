# Final Project of course Python+Selenium+PyTest.
Финальный проект курса "[Автоматизация тестирования с помощью Selenium и Python](https://stepik.org/course/575)"
____
ОС: Windows 10 x64

Версия Python: 3.7.6

IDE: PyCharm 2019.3
____

## Описание файлов и папок

1. Папка **`pages`**: содержит файлы Page Object.
    1. Файл **`base_page.py`**: базовая страница, от которой будут унаследованы все остальные классы. Описаны методы, которые применяются в проекте (переход в корзину, на страницу логина; реализация поиска элементов: представлен, отсутствует или исчезает; метод для открытия страницы; проверка авторизации пользователя; наличие ссылки на логин и прохождения капчи). Методы завернуты в класс, чтобы было удобно импортировать. 
    2. Файл **`basket_page.py`**: содержит проверки, что корзина пуста и есть сообщение об этом.
    3. Файл **`locators.py`**: содержит локаторы в виде констант. Локаторы каждой отдельной страницы завёрнуты в класс, чтобы было удобно импортировать.
    4. Файл **`login_page.py`**: содержит метод регистрации нового пользователя, проверки корректности ссылки на страницу логина, наличия форм регистрации и входа.
    5. Файл **`main_page.py`**: не содержит методов, поэтому реализована заглушка (вызов конструктора класса предка и передачи ему всех тех аргументов, которые мы передали в конструктор MainPage). Класс этот - условный MainPage - наследник класса BasePage, чтобы можно было пользоваться методами, описанными в `base_page.py`.
    6. Файл **`product_page.py`**: содержит методы добавления в корзину со страницы товара и проверку ожидаемого результата (название и цена добавленного товара соответствует представленному в корзине), проверки исчезновения элементов и отсутствия элементов (о добавлении товара в корзину).
2. Файл **`__init__.py`**: для работы относительных импортов.
3. Файл **`conftest.py`**: для хранения часто употребимых фикстур и хранения глобальных настроек (выбор браузера, языка страницы; открытие и закрытие экземпляра браузера).
4. Файл **`pytest.ini`**: содержит метки тестов проекта
5. Файл **`requirements.txt`**: содержит список пакетов и их версии, которые используются в проекте.
6. Файл **`test_main_page.py`**: тест-кейсы. Запускаем с помощью pytest. Содержит проверки, что гость видит ссылку и может перейти на страницу логина; что при открытии корзины с главной страницы гость видит пустую корзину и сообщение об этом.
7. Файл **`test_product_page.py`**: тест-кейсы. Запускаем с помощью pytest. Проверки:
    1. Гость может добавить товар в корзину и проверка корректности добавления товара (название, цена).
    2. Три реализации проверки отсутствия сообщений об успехе (товары не были добавлены).
    3. Гость может перейти на страницу логина с любой страницы.
    4. Гость открывает главную страницу, переходит в корзину, видит пустую корзину и сообщение об этом.
    5. Регистрация нового пользователя и проверка, что отсутствует сообщение об успехе (товары не были добавлены).
    6. Регистрация нового пользователя и проверка, что пользователь может добавить товар в корзину.