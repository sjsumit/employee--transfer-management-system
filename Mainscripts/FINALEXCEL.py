Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:05:16) [MSC v.1915 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import openpyxl
>>> wb = openpyxl.load_workbook('sumit.xlsx')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    wb = openpyxl.load_workbook('sumit.xlsx')
  File "C:\Users\SUNIL JAIN\AppData\Local\Programs\Python\Python37-32\lib\site-packages\openpyxl\reader\excel.py", line 174, in load_workbook
    archive = _validate_archive(filename)
  File "C:\Users\SUNIL JAIN\AppData\Local\Programs\Python\Python37-32\lib\site-packages\openpyxl\reader\excel.py", line 121, in _validate_archive
    archive = ZipFile(filename, 'r', ZIP_DEFLATED)
  File "C:\Users\SUNIL JAIN\AppData\Local\Programs\Python\Python37-32\lib\zipfile.py", line 1204, in __init__
    self.fp = io.open(file, filemode)
FileNotFoundError: [Errno 2] No such file or directory: 'sumit.xlsx'
>>> wb = openpyxl.load_workbook('C:/Users/SUNIL JAIN/Desktop/Python/Mainscripts/sumit.xlsx')
>>> sheet = wb.get_sheet_by_name('Sheet1')

Warning (from warnings module):
  File "__main__", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> sheet = wb["Sheet1"]
>>> sheet['A1']
<Cell 'Sheet1'.A1>
>>> sheet['A1'].value
'user 1'
>>> c = sheet['B1']
>>> c.value
SyntaxError: multiple statements found while compiling a single statement
>>> c = sheet['B1']
>>> c.value
'password 1'
>>> sheet['A2'].value
'user 2'
>>> sheet['B2'].value
'password 2'
>>> sheet['A3'].value
'user 3'
>>> sheet['B3'].value
'password 3'
>>> sheet['A4'].value
'user 4'
>>> sheet['B4'].value
'password 4'
>>> sheet['A5'].value
'user 5'
>>> sheet['B5'].value
'password 5'
>>> sheet['A6'].value
>>> sheet['B6'].value
>>> 
