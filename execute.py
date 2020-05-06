from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from os.path import sep
from pathlib import Path
from random import choice, random
from time import sleep
from json import dumps, loads

accounts = [
    {"username": "Fernando93Gomez", "email": "michal@telegmail.com", "password": "p8MQutPTHRp9@o"},
    {"username": "Fernando93Gomez", "email": "michal@telegmail.com", "password": "p8MQutPTHRp9@o"}
]

typeMinCharPerMinute = 200 # 60 secs / 180 characters
typeMaxCharPerMinute = 280 # 60 secs / 180 characters

minWindowSize = 720
maxWindowSize = 1080

class TinderGiveawayBot():
    cookiesClicked = False

    def __init__(self):
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
        self.driver.delete_all_cookies()
        self.driver.set_window_size( minWindowSize + ( random() * (maxWindowSize-minWindowSize)), minWindowSize + ( random() * (maxWindowSize-minWindowSize)))
        self.driver.set_window_position(0,0)


    def select_user(self, account):
        self.selectedAccount = account

    def goTwitter(self):
        self.driver.get("https://twitter.com/")
        self.randomSlow(2.5, 5)

    def goTwitterHome(self):
        self.driver.get("https://twitter.com/home")
        self.randomSlow(2.5, 5)

    def executeTwitterLogin(self):
        self.driver.get("https://twitter.com/login")
        self.randomSlow(2.5, 5)

        
        if random() > 0.5:
            self._removeCookiesBanner()

        usernameField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        self.send_keys_slowed(usernameField, self.selectedAccount[choice(["username", "email"])])
        self.randomSlow(0.5, 2)

        if self.cookiesClicked != True and random() > 0.5:
            self._removeCookiesBanner()

        passwordField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        self.send_keys_slowed(passwordField, self.selectedAccount["password"])
        self.randomSlow(0.5, 2)

        if self.cookiesClicked != True:
            self._removeCookiesBanner()

        loginButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div')
        loginButton.click()
        self.randomSlow(2.5, 5)
        
    def _removeCookiesBanner(self):
            try:
                self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[2]').click()
                self.randomSlow(0.5, 2)
            finally:
                self.cookiesClicked = True

    def tweet(self, text):
        tweetField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweetField.click()
        self.randomSlow(0.5, 1)
        self.send_keys_slowed(tweetField, text)
        self.randomSlow(0.5, 2)

        tweetButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')
        tweetButton.click()
    

    def saveCookies(self):
        with open(f"sessions/{self.selectedAccount['username']}-cookies.txt", "w+") as session_file:
            session_file.write( dumps( self.driver.get_cookies()) )

    def recoverCookies(self):
        try:
            with open(f"sessions/{self.selectedAccount['username']}-cookies.txt", "r") as session_file:
                cookies = loads( session_file.read() )
                for i in cookies:
                    self.driver.add_cookie(i)
        except:
            pass


    def send_keys_slowed(self, element, text: str):
        for i in text:
            element.send_keys(i)
            waitUntilNextChar = 60 / (typeMinCharPerMinute + (random() * (typeMaxCharPerMinute-typeMinCharPerMinute)) )
            sleep(waitUntilNextChar)

    def randomSlow(self, min: float, max: float):
        sleep ( min + (random() * (max-min)))


bot = TinderGiveawayBot()

account = choice(accounts)
bot.select_user(account)

bot.goTwitter()
bot.recoverCookies()
bot.goTwitterHome()

if bot.driver.current_url != "https://twitter.com/home":
    bot.driver.delete_all_cookies()
    bot.executeTwitterLogin()
    bot.saveCookies()
