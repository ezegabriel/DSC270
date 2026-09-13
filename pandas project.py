import pandas as pd

#1
q1 = pd.read_csv("C:/Users/HP/OneDrive/Desktop/DSC 270/wsl_2022-2023.csv")
#print(q1)

#2
print(q1["Goals"].sum())

#3
new_df = q1.groupby("Team")["Goals"].sum()
print(new_df)

#4
q4 = q1.copy()
q4.dropna(inplace = True)
print(q4["Goals"].sum())

#5
q5 = q4.copy()
q5.drop_duplicates(inplace = True)
print(q5["Goals"].sum())

#6
print(q5.describe())

#7
print("lookdown")
print(q5)
print(q5[q5["Player"] == "Bethany England"].index.values)

#8
# Simply, those two are rows are not actually duplicates of one another.
# They contain unique values.

#9
q9 = q5.copy()
q9.set_index("Player", inplace = True)
print(q9)

#10
print(q9.loc["Megan Finnigan"])

#11
print(q9.loc["Rachel Daly", "Goals"])

#12
q9["Discipline"] = 4*q9["Red"] + q9["Yellow"]
print(q9)

#13
q13 = q9[["Team", "Discipline"]]
print(q13)

#14
q14 = q13.sort_values(by = ["Discipline", "Player"], ascending = [False, True])
print(q14)

#15
new_df = q14.groupby("Team")["Discipline"].sum()
print(new_df)

#16
q16 = q13[q13["Discipline"] > 0]
print(q16)

#17
data = {"Player": ["Beth Mead", "Hayley Raso", "Guiro Reiten"], "Team": ["arsenal", "everton", "chelsea"], "Discipline": [6, None, 2]}
q17 = pd.DataFrame(data)
q17.set_index("Player", inplace=True)
print(q17)

#18
q17.fillna(q17["Discipline"].mean(), inplace=True)
print(q17)

#19
q19 = pd.concat([q16,q17])
print(q19)

#20
def fix_team_name(name):
    new = ""
    if " " in name:
        i_space = name.find(" ")
        new += name[0].upper() + name[1:i_space + 1] \
        + name[i_space + 1].upper() + name[i_space + 2 :]
    else:
        new += name[0].upper() + name[1:]
    return new

q19["Team"] = q19["Team"].map(fix_team_name)
print(q19)
