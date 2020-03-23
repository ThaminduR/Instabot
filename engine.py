import data
import datetime
import accountHandle

def init(webdriver):
    data.init()
    accountHandle.login(webdriver)

def update(webdriver):
    starttime = datetime.datetime.now()

    while True:

        accountHandle.follow_people(webdriver)

        endtime = datetime.datetime.now()
        elapsed = endtime - starttime

        starttime - datetime.datetime.now()