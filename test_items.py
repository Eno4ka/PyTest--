link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_add_to_cart_button(browser):
    browser.get(link)
    browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")