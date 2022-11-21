import pandas as pd

with open("scores.txt","r") as f:
    file = f.readlines()
    file = [i.replace("\n","").split(": ") for i in file]

en = "abcdefghijklmnopqrstuvwxyz"
ge = "აბცდეფგჰიჯკლმნოპქრსტუვწხყზ"
alph = dict(zip(en,ge))
alph["ცჰ"] = "ჩ"
alph["კრ"] = "ქრ"
alph["სჰ"] = "შ"
alph["კჰ"] = "ხ"
alph["დზ"] = "ძ"
alph["პხ"] = "ფხ"
alph["ტს"] = "ც"




names = [(i[0].split()[1]+" "+i[0].split()[0]).lower() for i in file]

for en,ge in alph.items():
    names = [ i.replace(en,ge) for i in names]


quiz_scores = [int(i[1].split("-")[1]) for i in file]
lab_scores = [int(i[1].split("-")[0]) for i in file]
mid_1 = [int(i[1].split("-")[2]) for i in file]
mid_2 = [int(i[1].split("-")[3]) for i in file]
final = [int(i[1].split("-")[4]) for i in file]

df = pd.DataFrame(names, columns = ['სახელი'])
df["ლაბის ქულა"] = lab_scores
df["ქვიზის ქულა"] = quiz_scores
df["შუალედური 1"] = mid_1
df["შუალედური 2"] = mid_2
df["ფინალური"] = final

df["ჯამური ქულა"] = df["ლაბის ქულა"] + df["ქვიზის ქულა"] + df["შუალედური 1"]+ df["შუალედური 2"]+ df["ფინალური"]
df1 = df[["სახელი","ჯამური ქულა"]].sort_values("ჯამური ქულა", ascending=False).reset_index(drop=True)
df2 = df.sort_values("სახელი").reset_index(drop=True)

df1.to_excel("leaderboard.xlsx")
df2.to_excel("result.xlsx")

