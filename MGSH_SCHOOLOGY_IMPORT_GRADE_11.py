# Imports
from selenium import webdriver
import win32com.client
import time
import csv
import os
autoit = win32com.client.Dispatch("AutoItX3.Control")
from selenium.webdriver.common.keys import Keys
from Login import login
from SchoologyControl import SchoologyControl
from GenerateGroupFile import generateGroupFile

# Globals
browser = webdriver.Chrome('/Users/zechaaron/Documents/AD/chromedriver')  # open Chrome Window
groupName = '2019-20 MGSH Juniors'
groupCSV = 'MGSH_Students_GR11.csv'
groupTXT = 'MGSH_Students_GR11.txt'
autoITScript ='MGSH_GR11.exe'

# Program Start
generateGroupFile(groupTXT,groupCSV,'MGSH','11')
time.sleep(4)
# Start up the web browser and open Schoology
login(browser)
# Process the Schoology tasks
SchoologyControl(browser,groupName,autoITScript)
