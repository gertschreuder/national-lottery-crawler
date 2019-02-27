
from selenium.webdriver.chrome.options import Options

class Webdriver(object):
    @staticmethod
    def getOptions():
        """
        Headless browser driver options
        """
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        return options

    @staticmethod
    def getElementText(browser, xpath):
        """
        Get text from element helper
        """
        elem = browser.find_elements_by_xpath(xpath)
        if len(elem) > 0:
            return elem[0].text
        else:
            return ""
