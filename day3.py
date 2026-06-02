print("Helo World")

import pandas as pd 
import numpy as np
print(" All packages imported successfully")
print("pandas version:",pd.__version__)
print("Numpy version:", np.__version__)

# view Data  
print("First 5 rows")
print(df.head(5))
# view list rows 
print("\n last 2 rows:")
print(df.tail(7))
# 
print("\nStatistical Summary:")
print(df.describe())
print("\n Missing Values :")
print(df.isnull().sum())
print("\n Check for Nam Values:")
print(df.isna().sum)
print("\n Dublicate Rows:")
print(df.duplicated().sum())

data = {
    'student_name':['Alice','Bob','Charlie','Diman','Eve','Alice'],
    'Hours_student':[5,8,3,10,6,5],
    'previous_score':[65,85,55,92,54,65],
    'attendance':[80,90,70,85,95,80],
    'sleep_hour':[7.8,6.8,6.9,4.7,9.8,7.8],
    'extracurricular':['yes','No','yes','No','yes','yes'],
    'parent_education':['Bachelor','Master','High score','Bachelor','High school','Bachelor']
    
}

df = pd.DataFrame(data)
print("Student performance DataForm;")
print(df)

# Basic dataForm Information
print("\nDataform Shape:",df.shape[0],"rows,",df.shape[1],"columns")
print("Column names:",df.columns.to_list())
print("Data types:\n",df.dtypes)
# print(df.info())