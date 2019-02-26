import utils.constants as constants

class Ball(object):
   def __init__(self, name, val):
      self.Name = name
      self.Value = val

class GameMapper(object):
   def __init__(self, browser):
      self.browser = browser
      self.draw = None
      self.date = None
      self.type = None
      self.result = []

   def map(self, page):
      self.draw = self.getElementText(constants.gameDrawPath % page)
      self.date = self.getElementText(constants.gameDatePath % page)
      self.type = self.getElementText(constants.gameTypePath % page)
      self.result = self.ResolveBalls(page)

   def ResolveBalls(self, page):
      items = []
      i = 1
      results = self.getElements(constants.gameResultPath % page)
      last = len(results)
      for r in results:
         name = 'Bonus Ball' if last == i  else 'Ball %s' % i
         ball = Ball(name, r)
         items.append(ball)
         i = i + 1
      return items

   def getElements(self, xpath):
      items = []
      elems = self.browser.find_elements_by_xpath(xpath)
      for elem in elems:
         itemRange = elem.text.split('\n')
         items.extend(itemRange)
      return items

   def getElementText(self, xpath):
      """
      Get text from element helper
      """
      elem = self.browser.find_elements_by_xpath(xpath)
      if len(elem) > 0:
         return elem[0].text
      else:
         return ""
