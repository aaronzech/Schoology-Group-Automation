from selenium import webdriver
from selenium.webdriver.firefox.service import Service
import win32com.client
import time
import csv
import os
from Login import login
from SchoologyControl import SchoologyControl
from GenerateGroupFile import generateGroupFile

#autoit = win32com.client.Dispatch("AutoItX3.Control")

from selenium.webdriver.common.keys import Keys

# Globals
# Globals
s=Service('C:/Users/zechaaron/Downloads/geckodriver.exe')
browser =  webdriver.Firefox(service=s)
groupName = 'PC CRC & Counseling'
groupCSV = 'PCSH_Students.csv'
groupTXT = 'PCSH_Students.txt'
autoITScript ='FileUpload.exe'

# Program Start
generateGroupFile(groupTXT,groupCSV,'PCSH','PCSH-ALL')
time.sleep(4)
# Start up the web browser and open Schoology
login(browser)
time.sleep(4)
# Process the Schoology tasks
SchoologyControl(browser,groupName,autoITScript)