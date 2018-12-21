##AAI Main Copyright Script
##Group Script


from classes.laptop import Utility

print ("Welcome to AAI")

loop = 'true'
while(loop == 'true'):
    user = input("Username Please : ") 
    password = input("Password Please : ")
    fileName = 'sumit.xlsx'
    sheetName = 'Sheet1'
    Utility.ParseExcel(user, password, fileName, sheetName)

    
                                         




    
