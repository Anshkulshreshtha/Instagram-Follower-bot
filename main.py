from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service


e_mail = "your emial id"
pswd = "your password"

similar = "virat.kohli"  #name of annother profile to increase inc follower

chrome_driver_path = "c:\development\chromedriver.exe"

sleep(2)

class InstaFollower:
    def __init__(self,path):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.get("https://www.instagram.com/")

    def follow(self):
        sleep(2)
        all_buttons = self.driver.find_elements(By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/div[3]/button")
        for button in all_buttons:
            if button.text != "Follow":
                pass
            else:
                button.click()
                sleep(2)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{similar}")
        sleep(2)
        Followers = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a")
        Followers.click()

        bar = self.driver.find_element(By.CSS_SELECTOR,'isgrP')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", bar)
            sleep(2)

    def login(self):
        sleep(5)
        login_via_fb = self.driver.find_element(By.XPATH,"/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[5]/button/span[2]")
        login_via_fb.click()
        sleep(2)
        Email = self.driver.find_element(By.ID, "email")
        Password = self.driver.find_element(By.ID, "pass")
        sleep(2)
        Email.send_keys(e_mail)
        Password.send_keys(pswd)
        Password.send_keys(Keys.ENTER)
        sleep(7)


service = Service(chrome_driver_path)
bot = InstaFollower(chrome_driver_path)
bot.login()
bot.find_followers()
bot.follow()
