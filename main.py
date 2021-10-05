import PythonTableModule
"""
File Name: main.py
Description: This file serves as a test for the PythonTableModule
"""

def main():
  headerList = ["This","Is","A","Test"]
  fieldList = []
  
  for index in range(126):
    fieldList.append(index)
  PythonTableModule.createAndPrintTable(headerList,fieldList)
  
if __name__ == "__main__":
  main()
