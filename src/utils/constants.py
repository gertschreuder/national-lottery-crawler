chromeDriverPath = r"/usr/bin/chromedriver"
outputPath = r"home/gert/git/national-lottery-crawler/output"

crawlerUrls = [
    r"https://www.nationallottery.co.za/lotto-history",
    r"https://www.nationallottery.co.za/lotto-plus-1-history",
    r"https://www.nationallottery.co.za/lotto-plus-2-history",
    r"https://www.nationallottery.co.za/powerball-history",
    r"https://www.nationallottery.co.za/powerball-plus-history"
]

fromDateBtnPath =r"//input[@id='fromDate']"
switchBtnPath =r"//table[@class=' table-condensed']/thead/tr[1]/th[@class='datepicker-switch']"
yearBtnPath =r"//div[@class='datepicker-months']/table[@class='table-condensed']/thead/tr/th[@class='datepicker-switch']"
oldBtnPath =r"//tbody/tr/td/span[@class='year old']"
monthBtnPath =r"//span[@class='month'][1]"
dayBtnPath =r"//tr[1]/td[@class='day'][1]"

toDateBtnPath =r"//input[@id='toDate']"
todayBtnPath =r"//td[@class='today day']"

searchBtnPath =r"//a[@id='search']/div[@class='btnBox']"

nextBtnPath =r"//a[@class='next']/i[@class='fa fa-angle-right']"

gameDrawPath =r"//div[@id='dataCounter-%s']/div[@class='col col1']/div[@class='dataVal dataVal1']"
gameDatePath =r"//div[@id='dataCounter-%s']/div[@class='col col2']/div[@class='dataVal dataVal1']"
gameTypePath =r"//div[@id='dataCounter-%s']/div[@class='col col3']/div[@class='dataVal dataVal1']"
gameResultPath =r"//div[@id='dataCounter-%s']/div[@class='col col4']/div[@class='dataVal dataVal1']/div[@class='resultBalls']/ul[@class='ballsList lotto']"
