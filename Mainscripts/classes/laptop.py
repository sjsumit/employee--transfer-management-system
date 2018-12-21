import openpyxl
import os
class Utility:                                        
        def ParseExcel(user, password, fileName, sheetName):
                cwd = os.getcwd()
                wb = openpyxl.load_workbook (fileName)
                sheet = wb[sheetName]
                numbers = [1,2,3,4,5]
                for val in numbers:
                        userRow = 'A'+ str(val)
                        userName = sheet[userRow].value
                        passwordRow = 'B' + str(val)
                        userPassword = sheet[passwordRow].value
                        if user == userName and password == userPassword:
                                print("Welcome "+ user)
                                return 'ok'
                                         
