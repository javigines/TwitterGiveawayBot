
class TwitterCommon():

    twitterMainURL = "https://twitter.com"
    twitterHomeURL = "https://twitter.com/home"
    twitterLoginURL = "https://twitter.com/login"
    twitterAppealURL = "https://help.twitter.com/forms/general?subtopic=suspended"

    def __init__(self, driver, humanizedUtils):
        self.driver = driver
        self.humanizedUtils = humanizedUtils

    def goMain(self):
        self.driver.get( self.twitterMainURL )
        self.humanizedUtils.randomSlow(2.5, 5)

    def goHome(self):
        self.driver.get( self.twitterHomeURL )
        self.humanizedUtils.randomSlow(2.5, 5)

    def goLogin(self):
        self.driver.get( self.twitterLoginURL )
        self.humanizedUtils.randomSlow(2.5, 5)

    def isAccountFlaggedLocked(self):
        return False