import pandas as pd
import re
import numpy as np
from sqlalchemy import create_engine

## Phone Validation Function
def phoneValid(number):
    
    if(len(number)==10 and number.isdigit()):
        output = re.findall(r"^[789]\d{9}$",number)
        if(len(output)==1):
            return True
        else:
            return False
    else:
        return False

#Email Validation Function
def emailValid(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if(re.search(regex, email)):
        return True
    else:
       return False

#PinCode validation Code
def pinValid(pin):
    regex_integer_in_range = r"^[1-9][\d]{5}$"	
    regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"	
    return (bool(re.match(regex_integer_in_range, pin)) 
    and len(re.findall(regex_alternating_repetitive_digit_pair, pin)) < 2)


# Address Valid must have 5 or more characters
def addressValid(addre):
    if len(addre)>6:
        return True
    else:
         return False



# reads CSV file 
df = pd.read_csv('sample.csv',error_bad_lines=False) # ,usecols=cols)

#defingind list to append output of validation n later directing putting it in Status coloumn
List=[]
#creating status coloumn
df['status']=''

#defining DataType of alll coloumns to be string to match Regex in functions
df = df.astype(np.str_)

#Iterate data row by row
for index, row in df.iterrows():
    if(phoneValid(row['Number'])==True & emailValid(row['Email'])==True & addressValid(row['Address'])==True & pinValid(row['Pincode'])==True ):
        b='True'
        List.append(b)
    else:
        b='False'
        List.append(b)

#appending List in status column
df['status'] = pd.DataFrame(List, columns=['status'])


#creating engine
engine = create_engine('mysql+mysqlconnector://root:oreo0008@localhost/practice'.format(user='root', password='oreo0008', server='localhost', database='practic'))

#uploading to sql
df.to_sql('AutomateData', con=engine) 

print("Uploaded")




 