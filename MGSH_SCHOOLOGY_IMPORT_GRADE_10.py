# Imports
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import win32com.client
import time
import csv
import os
from Login import login
from SchoologyControl import SchoologyControl
from GenerateGroupFile import generateGroupFile
from selenium.webdriver.common.keys import Keys


# Globals
s=Service('C:/Users/zechaaron/Downloads/geckodriver.exe')
browser =  webdriver.Firefox(service=s)
groupName = '2022-23 Grade 10'
groupCSV = 'MGSH_Students_GR10.csv'
groupTXT = 'MGSH_Students_GR10.txt'
autoITScript ='MGSH_GR10.exe'
clearEnrollments = False
# Program Start
generateGroupFile(groupTXT,groupCSV,'MGSH','10')
time.sleep(4)
# Start up the web browser and open Schoology
login(browser)
# Process the Schoology tasks
SchoologyControl(browser,groupName,groupCSV,clearEnrollments)