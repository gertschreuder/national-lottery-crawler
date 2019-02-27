# pylint: disable=E0401,E0611
from selenium import webdriver
import time
import utils.constants as constants
from utils.repo import Repository
from utils.serialize import Serialize
from utils.webdriver import Webdriver
from mappers.gameMapper import GameMapper

class LottoCrawler(object):
    def __init__(self):
        self.browser = webdriver.Chrome(constants.chromeDriverPath, chrome_options=Webdriver.getOptions())        

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
                    pages = Webdriver.getElementText(self.browser, "//ul[@id='pag']").split('\n')

                    if  len(pages) == 0 or len(games) == int(pages[len(pages) - 1]): break

                    for page in pages:
                        game = GameMapper()
                        game.map(page, self.browser)
                        game.type = url.split('/')[len(url.split('/')) - 1] #FIXME: this mapping is buggy
                        item = Serialize.jsonDumps(game)
                        games.append(item)

                        nextElem[0].click()
                        time.sleep(self.delay)
                    if  'disabled' in self.browser.find_elements_by_xpath("//li[@id='next']")[0].get_attribute('class'):
                        do = False
                        break

                Repository.save(games)

        except Exception as ex:
            print(ex)
            self.browser.quit()    

if __name__ == '__main__':
    a = LottoCrawler()
    a.run()