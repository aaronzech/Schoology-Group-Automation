Import-Module ActiveDirectory
Get-ADUser -SearchBase "OU=High School,OU=Schools,OU=AllUsers,DC=core,DC=oas,DC=ld" -Filter * -Properties DisplayName, Company, Created,Department, LastLogonDate, OfficePhone,physicalDeliveryOfficeName, EmailAddress | 
    Select-Object DisplayName, SamAccountName, Company, Created, LastLogonDate,Department, OfficePhone,physicalDeliveryOfficeName, EmailAddress, Enabled |
    Export-Csv C:\Users\zechaaron\Downloads\ADUsers.csv