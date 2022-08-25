import time
import secrets
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(browser):

    browser.get("https://osseo.schoology.com/import/group_enrollments")
    time.sleep(1) # delay for more reliablity
    # Locate Username Box
    userName = browser.find_element(By.ID,"form-signin-username")

    userName.send_keys(secrets.username)

    time.sleep(0.25) # delay for more reliablity

    # Locate Password Box
    passwordBox = browser.find_element(By.ID,'form-signin-password')

    passwordBox.send_keys(secrets.password)

    #browser.find_element(By.CLASS_NAME,'btn -success _pull-right _cursor-pointer')  # find log in button

    passwordBox.send_keys(Keys.RETURN)

    #elem = browser.find_element(By.CLASS_NAME,'btn -success _pull-right _cursor-pointer')

    #elem.click()  # click log in button

    print("Login Finished\n")
    time.sleep(6)  # delay for more reliablitiy