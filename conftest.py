import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="ru")


@pytest.fixture(scope="function")
def browser(request):
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': "es"})
    language = request.config.getoption("language")
    if language == "ru":
        print("\nstart ru language for test..")
        browser = webdriver.Chrome(options=options)
    elif language == "es":
        print("\nstart es language for test..")
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or es")
    yield browser
    print("\nquit browser..")
    browser.quit()