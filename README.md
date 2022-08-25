# Schoology-Group-Automation
Selenium / Python / AutoIT / Powershell - Automate Schoology group uploads via fresh active directory pulls

**Inspiration:** Some schools needed to have their schoology groups updated more frequently, and only admins can bulk update groups. I came of with this way to run a windows batch file to grab an updated user list from active direcotry and use python and selneium web driver to automate the schoology group update.

**Directions:**
python -m pip install pywin32
<br>
Run Powershell script - AD_Pull.ps1 - This is generate a CSV file export from Active Directory.

