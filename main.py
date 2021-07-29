from selenium import webdriver


IG_USERNAME = "ENTER USERNAME"
IG_PASS = "ENTER PASSWORD!"
SIMILAR_ACCOUNT = "ACCOUNT YOU TO FOLLOW ON IG"
CHROME_DRIVER_PATH = "ENTER CHROME DRIVER PATH"


class InstaFollow:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)