from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import sep
from pathlib import Path

from time import sleep
from random import choice, random

from modules.twitter.common import TwitterCommon
from modules.twitter.logIn import TwitterLogIn
from modules.others.humanizedUtils import HumanizedUtils

accounts = [
    {"username": "Fernando93Gomez", "email": "michal@telegmail.com", "password": "p8MQutPTHRp9@o"}
]

typeMinCharPerMinute = 200 # 60 secs / 180 characters
typeMaxCharPerMinute = 280 # 60 secs / 180 characters

minWindowSize = 720
maxWindowSize = 1080

class TinderGiveawayBot():

    def __init__(self):
        self._initWebdriver()
        self.humanizedUtils = HumanizedUtils(typeMinCharPerMinute, typeMaxCharPerMinute)
        self.twitterCommon = TwitterCommon(self.driver, self.humanizedUtils)

        self.twitterLogIn = TwitterLogIn(self.driver, self.twitterCommon, self.humanizedUtils)

    def _initWebdriver(self):
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('-safe-mode')
        #firefox_options.add_argument("-private")
        firefox_options.add_argument("-foreground")

        # Remove Javascript
        profile = webdriver.FirefoxProfile()
        """ 
        profile.DEFAULT_PREFERENCES['frozen']['javascript.enabled'] = False
        profile.set_preference("app.update.auto", False)
        profile.set_preference("app.update.enabled", False)
        profile.update_preferences() """

        self.driver = webdriver.Firefox(
            executable_path=f"{Path(__file__).parent.absolute()}{sep}drivers{sep}geckodriver.exe",
            options=firefox_options,
            firefox_profile=profile
        )

        sleep(1)
        self.driver.delete_all_cookies()
        self.driver.set_window_size( minWindowSize + ( random() * (maxWindowSize-minWindowSize)), minWindowSize + ( random() * (maxWindowSize-minWindowSize)))
        self.driver.set_window_position(0,0)



botInstance = TinderGiveawayBot()

account = choice(accounts)
botInstance.twitterLogIn.execute(account)

if( botInstance.twitterCommon.isAccountFlaggedLocked() ):
    print("Flagged")
else:
    print("Logged")