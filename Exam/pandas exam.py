import pandas as pd
#1
q1a, q2b = pd.read_csv("cerealA.csv"), pd.read_csv("cerealB.csv")
#print(q1a)

#2
q2 = pd.concat([q1a,q2b])
#print(q2)

#3
q3 = q2.copy()
q3.dropna(inplace = True)
#print(q3)

#4
q4 = q3.copy()
q4.drop_duplicates(inplace = True)

#5
print(q4.describe())
print()

#6
q6 = q4.copy()
q6.set_index("name", inplace = True)
#print(q6)

#7
print("Number of calories for Trix:", q6.loc["Trix", "calories"])
print()
#8
print(q6.loc["Smacks"])
print()

#9
q6["Net_Carbs"] = q6["carbo"] - q6["fiber"]
#print(q6)

#10
print("Sum of all calories on 1 serving:", q6["calories"].sum())
print()

#11
q11 = q6.groupby("mfr")["calories"].sum()
#print(q11)

#12
q12 = q6[["mfr", "type", "calories"]]
#print(q12)

#13
q13 = q12.sort_values(by = ["calories", "mfr"], ascending = [False, False])
#print(q13)

#14
q14 = q12.copy()
def rename(mfr):
    if mfr == "N":
        mfr = "Nabisco"
    elif mfr == "G":
        mfr = "General Mills"
    elif mfr == "K":
        mfr = "Kellogs"
    return mfr
q14["mfr"] = q14["mfr"].map(rename)
#print(q14)

#15
q15 = pd.read_csv("cerealC.csv")
q15.fillna(q15["calories"].max(), inplace = True)

#16
print("List of index:", q15[q15["mfr"] == "K"].index.values)
