import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import win32com
import win32com.client
import autoit

#autoit = win32com.client.Dispatch("AutoItX3.Control")
#autoit = win32com.client.Dispatch("AutoItX3.Control")




def SchoologyControl(browser,groupName,groupCSV,clearEnrollments):

    # select enrollment type
    enrollmentType = browser.find_element(By.ID,'edit-enrollment-type')
    enrollmentType.click()
    enrollmentType.send_keys('m')
    enrollmentType.click()
    enrollmentType.send_keys(Keys.TAB)

    # Select Group to update
 
    
    
    
    select = browser.find_element(By.ID, "s2id_autogen1_search")
    select.send_keys(groupName)
    time.sleep(5)
    select.send_keys(Keys.ENTER)
    # select by visible text
    time.sleep(0.2)
    print("group selected")

    # check clear group enrollments
    if(clearEnrollments == True):
        clearExistingEnrollments = browser.find_element(By.ID,'edit-clear-enrollments')
        clearExistingEnrollments.click()

    time.sleep(2)  # delay for more reliablitiy
    
    # uploadFIle

    #Send file keys method
    file = browser.find_element(By.XPATH,"//*[contains(@id,'html5')][not(contains(@id, '_container'))]") # Dynamic Element - Look for 'HTML5' and does not contain 'container'
    file.send_keys("C:\\Users\\zechaaron\\OneDrive - Osseo Area Schools\\Documents\\AD\\"+groupCSV)
    #------------------------

    #attachFile = browser.find_element(By.ID,'upload-btn')
    #attachFile.click()
    # Call AutoIT
    #autoit.run("C:\\Users\\zechaaron\\Downloads\\Schoology-Group-Automation-master\\Schoology-Group-Automation-master\\FileUpload.exe")
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