import numpy as np
import pandas as pd

people = ["sara liang", "tony tao", "karen li", "michael crotty", "kobe zhang",
            "meng",  "james chen", "jordan li", "stephen dai", "kruthi thangali", 
            "oi srinualnad", "ravi patel"]

lecture = {"name":people, "andrewID":["placeholder"]*len(people), "Attention":[100]*len(people), 
        "Time In": ["placeholder"]*len(people), "Time Out":["placeholder"]*len(people), 
            "Talking Time":[10]*len(people), "Attendance Time":[60]*len(people)}

df = pd.DataFrame(lecture)
print(df)
KobeData = df.loc[people.index("kobe zhang")]
print(KobeData)
print(KobeData.loc["Attention"])

print(df["Talking Time"].mean())
newStudent = {"name": "alan hsu", "andrewID": "alanhsu", "Attention":100, 
        "Time In":"placeholder" , "Time Out": "placeholder", 
            "Talking Time":10, "Attendance Time":60}

df = df.append(newStudent, ignore_index=True)
print(df)

