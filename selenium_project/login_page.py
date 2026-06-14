
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    # Page URL
    URL = "https://the-internet.herokuapp.com/login"

    #Locators
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type=submit]")
    FLASH_MESSAGE = (By.ID, "flash")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")

    #Common actions
    def __init__(self, driver):
        self.driver = driver
    def open(self):
        self.driver.get(self.URL)
    
    def wait_visible(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    def get_flash_message(self):
        return self.wait_visible(*self.FLASH_MESSAGE).text.strip()
    
    # Page actions
    def login(self, username, password):
        self.wait_visible(*self.USERNAME_INPUT).send_keys(username)
        self.wait_visible(*self.PASSWORD_INPUT).send_keys(password)
        self.wait_visible(*self.LOGIN_BUTTON).click()

    def logout(self):
        self.wait_visible(*self.LOGOUT_LINK).click()  

     #Page elements visibility and attributes
    def is_username_input_visible(self):
        return self.wait_visible(*self.USERNAME_INPUT).is_displayed()
    
    def is_password_input_visible(self):
        return self.wait_visible(*self.PASSWORD_INPUT).is_displayed()

    def is_login_button_visible(self):
        return self.wait_visible(*self.LOGIN_BUTTON).is_displayed()    
    
    def get_password_input_type(self):
        return self.wait_visible(*self.PASSWORD_INPUT).get_attribute("type")