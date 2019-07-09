from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
"""
bot = webdriver.Firefox()
bot.get("https://twitter.com/")

 """


class TwitterBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.bot = webdriver.Firefox()

    def login(self):
        bot = self.bot
        bot.get("https://twitter.com/")
        time.sleep(3)
        email = bot.find_element_by_class_name('email-input')
        password = bot.find_element_by_name('session[password]')
        email.clear()
        password.clear()
        email.send_keys(self.username)
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(3)


ed = TwitterBot('jjsebastianfuertes@gmail.com', 'Aprendizcruel1995')
ed.login()
