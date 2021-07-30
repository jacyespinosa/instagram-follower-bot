from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time


IG_USERNAME = "ENTER USERNAME"
IG_PASS = "ENTER PASSWORD!"
SIMILAR_ACCOUNT = "ACCOUNT YOU TO FOLLOW ON IG"
CHROME_DRIVER_PATH = "ENTER CHROME DRIVER PATH"


class InstaFollow:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self):
        website = self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(5)
        '''
        LOG IN TO INSTAGRAM ACCOUNT. PAGES MAY LOAD SLOW, THEREFORE, IT IS SAFE TO ADD AN EXCEPTION TO PUT A SLEEP TIMER
        AND TRY ACCESSING THE ELEMENT AGAIN.
        '''
        try:
            enter_username = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
            enter_username.send_keys(f'{IG_USERNAME}')
            enter_pass = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
            enter_pass.send_keys(f'{IG_PASS}')
        except NoSuchElementException:
            time.sleep(1)

        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        log_in.click()
        time.sleep(5)

        '''SEARCH FOR A TARGET/DESIRED ACCOUNT THAT YOU WANT TO FOLLOW.'''
        try:
            search = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
            search.send_keys(f'{SIMILAR_ACCOUNT}')
            time.sleep(1)
            enter = self.driver.find_element_by_xpath(
                '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]')
            enter.click()
        except NoSuchElementException:
            time.sleep(1)

    def find_followers(self):
        time.sleep(10)
        '''CLICK ON THE FOLLOWING BUTTON TO ACCESS THE TARGET USER'S FOLLOWERS'''
        find = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        find.click()
        '''SINCE THE LIST OF FOLLOWERS IN THE POPUP IS ONLY LIMITED TO 15 VISIBLE USERS, NEED TO BE ABLE TO SCROLL
        DOWN TO SEE MORE FOLLOWERS (SCROLL DOWN ON THE POPUP NOT THE MAIN WEBPAGE).'''
        time.sleep(5)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(20):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(3)