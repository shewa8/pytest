import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find__card_button(browser):
    browser.get(link)

    # Для удобства, просто в строке ниже удалите "#"
    #time.sleep(30)

    basket_btn = len(browser.find_elements_by_class_name("btn-add-to-basket"))
    assert basket_btn > 0, 'Element isn\'t found'


