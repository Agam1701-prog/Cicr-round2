# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 13:30:20 2025

@author: Agam
"""
import pandas as pd
from tabulate import tabulate
contact_book={"Name":["Arun","Bani","Chandan","Danish"],
              "Phone":[1234936354,4567110837,6789993600,8901445489],
              "Email":["abc@gmail.com","def@gmail.com","pqr@gmail.com","xyz@gmail.com"]}
df=pd.DataFrame(contact_book,columns=["Name","Phone","Email"])
df.to_csv("C:\\contact_book\\contact_book.csv")
print(df)
headers=["Name","Phone","Email"]
print(tabulate(contact_book,headers=headers,tablefmt="fancy_grid"))

name = input("Enter name to search: ")
result = df[df["Name"].str.lower() == name.lower()]

if not result.empty:
    print(result)
else:
    print("Contact not found")