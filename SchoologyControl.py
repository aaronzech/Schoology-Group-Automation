import time

import win32com

autoit = win32com.client.Dispatch("AutoItX3.Control")

def SchoologyControl(browser,groupName,autoITScript):

    # select enrollment type
    enrollmentType = browser.find_element_by_id('edit-enrollment-type')
    enrollmentType.click()
    enrollmentType.send_keys('m')
    enrollmentType.click()

    # Select Group to update
    groupSelect = browser.find_element_by_id('edit-group-nid')
    groupSelect.click()
    groupSelect.send_keys(groupName)
    print("group selected")

    # check clear group enrollments
    clearExistingEnrollments = browser.find_element_by_id('edit-clear-enrollments')
    clearExistingEnrollments.click()

    time.sleep(2)  # delay for more reliablitiy
    # uploadFIle
    attachFile = browser.find_element_by_id('upload-btn')
    attachFile.click()
    # Call AutoIT
    autoit.run("C:\\Users\\zechaaron\\Documents\\AD\\"+autoITScript);
    # Submit
    time.sleep(8)
    submitButton = browser.find_element_by_id('edit-submit').click()
    print("File Submitted")

    # Match columns Page
    matchColumn = browser.find_element_by_id('edit-fields-school-uid-matched-attr')
    matchColumn.click()
    matchColumn.send_keys('Column 1')
    submitButton = browser.find_element_by_id('edit-submit').click()
    time.sleep(6)
    submitButton = browser.find_element_by_id('edit-submit').click()


    print("Program finished")