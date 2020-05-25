
from random import random, choice
from json import dumps, loads

class TwitterLogIn():
    cookiesClicked = False

    def __init__(self, driver, twitterCommon, humanizedUtils):
        self.driver = driver
        self.twitterCommon = twitterCommon
        self.humanizedUtils = humanizedUtils

    def execute(self, selectedAccount):
        self.selectedAccount = selectedAccount
        
        self.twitterCommon.goMain()
        self._recoverCookies()
        self.twitterCommon.goHome()

        
        if self.driver.current_url != self.twitterCommon.twitterHomeURL:
            self.driver.delete_all_cookies()
            self._executeTwitterLogin()
            self._saveCookies()


    def _executeTwitterLogin(self):
        self.twitterCommon.goLogin()

        if random() > 0.5:
            self._removeCookiesBanner()

        usernameField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[1]/label/div/div[2]/div/input')
        self.humanizedUtils.send_keys_slowed(usernameField, self.selectedAccount[choice(["u", "e"])])
        self.humanizedUtils.randomSlow(0.5, 2)

        if self.cookiesClicked != True and random() > 0.5:
            self._removeCookiesBanner()

        passwordField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[2]/label/div/div[2]/div/input')
        self.humanizedUtils.send_keys_slowed(passwordField, self.selectedAccount["p"])
        self.humanizedUtils.randomSlow(0.5, 2)

        if self.cookiesClicked != True:
            self._removeCookiesBanner()

        loginButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/form/div/div[3]/div')
        loginButton.click()
        self.humanizedUtils.randomSlow(2.5, 5)


    def _removeCookiesBanner(self):
            try:
                self.driver.find_element_by_xpath('/html/body/div/div/div/div[1]/div/div/div/div[2]').click()
                self.humanizedUtils.randomSlow(0.5, 2)
            finally:
                self.cookiesClicked = True
    

    def _saveCookies(self):
        with open(f"sessions/{self.selectedAccount['u']}-cookies.txt", "w+") as session_file:
            session_file.write( dumps( self.driver.get_cookies()) )

    def _recoverCookies(self):
        with open(f"sessions/{self.selectedAccount['u']}-cookies.txt", "r") as session_file:
            cookies = loads( session_file.read() )
            for i in cookies:
                self.driver.add_cookie(i)