import DavesDB as ddb
import matplotlib.pyplot as plt

#print("Selecting from players\n===========\n")
results = ddb.getData(sql = "SELECT * FROM players")

d_teamNames = {}
for row in range(len(results)):
    s_teamName = results[row][7]
    if s_teamName in d_teamNames.keys():
        d_teamNames[s_teamName] = d_teamNames[s_teamName] + 1
    else:
        d_teamNames[s_teamName] = 1

l_x = []
l_y = []

for teamName in d_teamNames.keys():
    #print(teamName, ": ", d_teamNames[teamName])
    l_x.append(teamName)
    l_y.append(d_teamNames[teamName])

#print(l_x)
#print(l_y)

plt.barh(l_x, l_y, height = .2, color = "red")
plt.xlabel("Number of Players")
plt.ylabel("Team")
plt.title("Frequency of Players on Teams")
plt.show()



