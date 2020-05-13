import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)
    time.sleep(30)
    btn = browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
    assert btn
