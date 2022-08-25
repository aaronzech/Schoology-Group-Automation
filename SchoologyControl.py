import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import win32com
import win32com.client
import autoit

#autoit = win32com.client.Dispatch("AutoItX3.Control")
#autoit = win32com.client.Dispatch("AutoItX3.Control")




def SchoologyControl(browser,groupName,autoITScript):

    # select enrollment type
    enrollmentType = browser.find_element(By.ID,'edit-enrollment-type')
    enrollmentType.click()
    enrollmentType.send_keys('m')
    enrollmentType.click()

    # Select Group to update
    select = Select(browser.find_element(By.ID,'edit-group-nid'))
    # select by visible text
    select.select_by_visible_text('PC CRC & Counseling')
    time.sleep(0.2)
    print("group selected")

    # check clear group enrollments
    clearExistingEnrollments = browser.find_element(By.ID,'edit-clear-enrollments')
    clearExistingEnrollments.click()

    time.sleep(2)  # delay for more reliablitiy
    # uploadFIle
    attachFile = browser.find_element(By.ID,'upload-btn')
    attachFile.click()
    # Call AutoIT
    autoit.run("C:\\Users\\zechaaron\\Downloads\\Schoology-Group-Automation-master\\Schoology-Group-Automation-master\\FileUpload.au3")
    #autoit.run("C:\\Users\\zechaaron\\Downloads\\Schoology-Group-Automation-master\\Schoology-Group-Automation-master\\"+autoITScript);
    # 
    # Submit
    time.sleep(8)
    submitButton = browser.find_element(By.ID,'edit-submit').click()
    print("File Submitted")

    # Match columns Page
    matchColumn = browser.find_element(By.ID,'edit-fields-school-uid-matched-attr')
    matchColumn.click()
    matchColumn.send_keys('Column 1')
    submitButton = browser.find_element(By.ID,'edit-submit').click()
    time.sleep(6)
    submitButton = browser.find_element(By.ID,'edit-submit').click()


    print("Program finished")