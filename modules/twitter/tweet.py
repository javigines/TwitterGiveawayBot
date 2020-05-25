
class TwitterTweet():

    def __init__(self, driver, twitterCommon, humanizedUtils):
        self.driver = driver
        self.twitterCommon = twitterCommon
        self.humanizedUtils = humanizedUtils
    
    def execute(self, text):
        if(self.driver.current_url != self.twitterCommon.twitterHomeURL):
            self.twitterCommon.goHome()

        tweetField = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweetField.click()

        self.humanizedUtils.randomSlow(0.5, 1)
        self.humanizedUtils.send_keys_slowed(tweetField, text)
        self.humanizedUtils.randomSlow(0.5, 2)

        tweetButton = self.driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]')
        tweetButton.click()
