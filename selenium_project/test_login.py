from selenium import webdriver
import pytest
from selenium_project.login_page import LoginPage

# Browser setup
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

    
#valid login
def test_valid_login(driver):    
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in login_page.get_flash_message()
    assert "/secure" in driver.current_url
    
    #test click back button after logout
def test_click_back_button_after_logout(driver):    
     login_page = LoginPage(driver)
     login_page.open()
     login_page.login("tomsmith", "SuperSecretPassword!")
     assert "You logged into a secure area!" in driver.page_source    
     login_page.logout()
     driver.back()
     assert "You logged into a secure area!"  in login_page.get_flash_message()
     driver.refresh()
     assert "You must login to view the secure area"  in driver.page_source

  #invalid login combinations  
@pytest.mark.parametrize("username,password,error_message", [
    ("tomsmith", "wrongpassword", "Your password is invalid!"),
    ("", "SuperSecretPassword!", "Your username is invalid!"),
    ("tomsmith", "", "Your password is invalid!"),
    ("", "", "Your username is invalid!")
])
def test_invalid_login_combinations(driver, username, password, error_message):
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login(username, password)
        assert error_message in login_page.get_flash_message()

# UI elements visibility and attributes
def test_login_page_elements_visibility(driver):
     login_page = LoginPage(driver)
     login_page.open()
     assert login_page.is_username_input_visible()
     assert login_page.is_password_input_visible()
     assert login_page.is_login_button_visible()
     
     #test password input type is password
     def test_password_input_type_is_password(driver):
        login_page = LoginPage(driver)
        login_page.open()
        assert login_page.get_password_input_type() == "password"