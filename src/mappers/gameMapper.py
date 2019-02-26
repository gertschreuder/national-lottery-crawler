import utils.constants as constants
from bson.objectid import ObjectId
import datetime

class Ball(object):
   def __init__(self, name, val):
      self.Name = name
      self.Value = val

class GameMapper(object):
   def __init__(self):
      self.draw = None
      self.date = None
      self.type = None
      self.result = []

   def generateId(self):
      gen_time = datetime.datetime.utcnow()
      return ObjectId.from_datetime(gen_time)

   def map(self, page, browser):
      self.id = self.generateId()
      self.draw = self.getElementText(constants.gameDrawPath % page, browser)
      self.date = self.getElementText(constants.gameDatePath % page, browser)
      self.type = self.getElementText(constants.gameTypePath % page, browser)
      self.result = self.ResolveBalls(page, browser)

   def ResolveBalls(self, page, browser):
      items = []
      i = 1
      results = self.getElements(constants.gameResultPath % page, browser)
      last = len(results)
      for r in results:
         name = 'Bonus Ball' if last == i  else 'Ball %s' % i
         ball = Ball(name, r)
         items.append(ball)
         i = i + 1
      return items

   def getElements(self, xpath, browser):
      items = []
      elems = browser.find_elements_by_xpath(xpath)
      for elem in elems:
         itemRange = elem.text.split('\n')
         items.extend(itemRange)
      return items

   def getElementText(self, xpath, browser):
      """
      Get text from element helper
      """
      elem = browser.find_elements_by_xpath(xpath)
      if len(elem) > 0:
         return elem[0].text
      else:
         return ""
