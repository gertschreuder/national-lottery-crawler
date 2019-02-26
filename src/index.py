# pylint: disable=E0401,E0611
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import json
import os
import pymongo
import multiprocessing
from multiprocessing import Pool
import utils.constants as constants
from mappers.gameMapper import GameMapper

class LottoCrawler(object):
    def __init__(self):
        self.browser = webdriver.Chrome(constants.chromeDriverPath, chrome_options=LottoCrawler.getOptions())        

    def run(self):       
        try:
            do = True
            maxPageRows = 10
            minPages = 1
            self.delay = 5
            pageRows = maxPageRows * minPages
            for url in constants.crawlerUrls:
                print(url)
                self.browser.get(url)
                time.sleep(self.delay)
                #from
                dropdown = self.browser.find_element_by_xpath(constants.fromDateBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.switchBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.yearBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.oldBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.monthBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.dayBtnPath)
                dropdown.click()

                #to
                dropdown = self.browser.find_element_by_xpath(constants.toDateBtnPath)
                dropdown.click()
                dropdown = self.browser.find_element_by_xpath(constants.todayBtnPath)
                dropdown.click()

                #search
                dropdown = self.browser.find_element_by_xpath(constants.searchBtnPath)
                dropdown.click()
                time.sleep(self.delay)
                
                games = []
                while(do):
                    #map
                    nextElem = self.browser.find_elements_by_xpath("//li[@id='next']/a[@class='next']")
                    pages = self.getElementText("//ul[@id='pag']").split('\n')

                    if  len(pages) == 0 or len(games) == int(pages[len(pages) - 1]): break

                    for page in pages:
                        game = GameMapper()
                        game.map(page, self.browser)
                        item = LottoCrawler.jsonDumps(game)
                        games.append(item)

                        nextElem[0].click()
                        time.sleep(self.delay)
                    if  'disabled' in self.browser.find_elements_by_xpath("//li[@id='next']")[0].get_attribute('class'):
                        do = False
                        break

                #fileName = constants.crawlerUrls[0].split('/')[len(constants.crawlerUrls[0].split('/')) - 1]
                #items = LottoCrawler.saveJsonDocument(r"%s/%s.json" % (constants.outputPath,fileName), games)
                LottoCrawler.save(games)

        except Exception as ex:
            print(ex)
            self.browser.quit()

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
    def saveJsonDocument(path: str, data, isMultiPro = False, m: str = 'w+'):
        """
        Converts data to json before saving to file
        """
        d = LottoCrawler.jsonDumps(data)
        if isMultiPro:
            d = d + ','
        LottoCrawler.fileWriter(path, d, m)
        return d

    @staticmethod
    def jsonDumps(data):
        if data is None:
            return data
        if hasattr(data, "__dict__"):
            data = data.__dict__
        item = {}
        for k, v in data.items():
            if isinstance(v, list):
                lys = []
                [lys.append(LottoCrawler.jsonDumps(i)) for i in v]
                item[k] = lys
            else:
                item[k] = v

        return item    

    @staticmethod
    def fileWriter(path: str, data, m = 'a+'):
        """
        Writes file to disk
        """
        abs_file_path = LottoCrawler.getFilePath(path)
        f = open(abs_file_path, m)
        f.write(data)

    @staticmethod
    def save(data):
        myclient = pymongo.MongoClient('172.30.0.2',username='admin', password='R3ste4rt!', connect=False, authMechanism='SCRAM-SHA-1')
        db = myclient["ithuba"]
        gameCol = db["game"]
        gameCol.insert_many(data)

    def getElementText(self, xpath):
        """
        Get text from element helper
        """
        elem = self.browser.find_elements_by_xpath(xpath)
        if len(elem) > 0:
            return elem[0].text
        else:
            return ""

if __name__ == '__main__':
    a = LottoCrawler()
    a.run()