import time
from selenium.common.exceptions import NoSuchElementException

def login(browser):

    browser.get("https://osseo.schoology.com/import/group_enrollments")
    time.sleep(4)  # delay for more reliablity

    browser.find_element_by_id('edit-mail-wrapper')

    # Locate Username Box
    userName = browser.find_element_by_id('edit-mail')

    userName.send_keys("sdfsd")

    time.sleep(0.1) # delay for more reliablity

    # Locate Password Box
    passwordBox = browser.find_element_by_id('edit-pass')

    passwordBox.send_keys("adfsd")

    browser.find_element_by_class_name('submit-span-wrapper')  # find log in button

    elem = browser.find_element_by_class_name('submit-span-wrapper')

    elem.click()  # click log in button

    print("Login Finished\n")
    time.sleep(6)  # delay for more reliablitiy